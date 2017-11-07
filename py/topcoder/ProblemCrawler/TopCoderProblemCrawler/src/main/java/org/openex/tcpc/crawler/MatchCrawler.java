package org.openex.tcpc.crawler;

import com.codepoetics.protonpack.StreamUtils;
import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.lang3.StringUtils;
import org.apache.log4j.PropertyConfigurator;
import org.openex.tcpc.bean.TCProblem;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import us.codecraft.webmagic.Page;
import us.codecraft.webmagic.Spider;
import us.codecraft.webmagic.pipeline.ConsolePipeline;
import us.codecraft.webmagic.selector.Selectable;

import java.io.File;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.util.List;
import java.util.stream.Collectors;

public class MatchCrawler extends BasicCrawler {
    private static final Logger logger = LoggerFactory.getLogger(MatchCrawler.class);

    public static void main(String[] args) {
        System.out.println(new File("log4j.properties").getAbsolutePath());
        PropertyConfigurator.configure("log4j.properties");
        logger.info("Starting...");
        Spider.create(new MatchCrawler())
                .addUrl("http://community.topcoder.com/stat?c=round_overview&er=5&rd=4715")
                .addPipeline(new ConsolePipeline())
                .addPipeline(new org.openex.tcpc.crawler.TCJsonFilePipeline("data"))
                .setDownloader(new TCDowloader())
                .thread(5).run();
    }

    @Override
    public void process(Page page) {
        if (!isValidPage(page)) {
            logger.error("page is invalid: " + page.getRequest().getUrl());
            return;
        }

        List<TCProblem> problems = StreamUtils.zipWithIndex(
                page.getHtml().css("td.bodyText > table > tbody > tr:nth-child(n+3)").nodes()
                        .stream()
                        .filter(node -> node.xpath("//td").nodes().size() == 7)
        ).map(v -> {
            Selectable node = v.getValue();
            int div = (int) (v.getIndex() / 3 + 1);

            String name = node.xpath("td/a/text()").get();
            String link = node.xpath("td/a//@href").get();
            TCProblem problem = new TCProblem();
            problem.setName(name);
            problem.setLink(link);

            List<String> problemTexts = node.xpath("td/text()").all();
            if (problemTexts != null && problemTexts.size() > 0) {
                try {
                    String level = problemTexts.get(0).replace("&nbsp;", "").trim().replaceAll("\\W", "");
                    if (level.equalsIgnoreCase("LevelOne")) {
                        problem.setLevel(1);
                    } else if (level.equalsIgnoreCase("LevelTwo")) {
                        problem.setLevel(2);
                    } else if (level.equalsIgnoreCase("LevelThree")) {
                        problem.setLevel(3);
                    }
                    String submission = problemTexts.get(2).replaceAll("[\\D.]", "").trim();
                    if (submission.length() > 0) {
                        problem.setSubmission(Integer.parseInt(submission));
                    }
                    String correct = problemTexts.get(3).replaceAll("[^\\d.]", "").trim();
                    if (correct.length() > 0) {
                        problem.setCorrectRatio(Float.parseFloat(correct));
                    }
                    String avgPts = problemTexts.get(4).replaceAll("[^\\d.]", "").trim();
                    if (avgPts.length() > 0) {
                        problem.setAvgPts(Float.parseFloat(avgPts));
                    }
                } catch (Exception e) {
                    System.err.println(e.getMessage());
                }
            }
            logger.info("Found problem: " + problem.toString());
            problem.setDiv(div);
            return problem;
        }).filter(s -> StringUtils.isNotBlank(s.getLink()))
                .collect(Collectors.toList());

        logger.info("problems: " + problems.toString());
        page.putField("problems", problems);
        String matchName = page.getHtml().css("body > table > tbody > tr > td.bodyText > table:nth-child(3) > " +
                "tbody > tr > td > form > select").xpath("//option[@selected]/text()").get();
        page.putField("name", matchName);
        page.putField("link", page.getRequest().getUrl());

        String matchMd5 = DigestUtils.md5Hex(page.getRequest().getUrl());
        problems.stream()
                .filter(problem -> !Files.exists(FileSystems.getDefault().getPath("data/problems/" + matchMd5 + "/",
                        DigestUtils.md5Hex(problem.getLink()) + ".json")))
                .forEach(problem -> {
                    Spider.create(new ProblemCrawler())
                            .addUrl(problem.getLink())
                            .addPipeline(new ConsolePipeline())
                            .addPipeline(new TCJsonFilePipeline("data/problems/" + matchMd5 + "/"))
                            .setDownloader(new TCDowloader())
                            .thread(5)
                            .run();
                });
    }

}
