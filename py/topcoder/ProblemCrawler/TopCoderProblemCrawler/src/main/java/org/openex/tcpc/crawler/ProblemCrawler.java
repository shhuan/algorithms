package org.openex.tcpc.crawler;

import org.apache.commons.lang3.StringEscapeUtils;
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
import java.lang.reflect.Field;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ProblemCrawler extends BasicCrawler {
    private final static Logger logger = LoggerFactory.getLogger(ProblemCrawler.class);

    @Override
    public void process(Page page) {
        if (!isValidPage(page)) {
            logger.error("page is invalid: " + page.getRequest().getUrl());
            return;
        }
        logger.info("processing problem {}", page.getRequest().getUrl());
        List<Selectable> nodes = page.getHtml().css("td.problemText > table > tbody > tr").nodes();
        TCProblem problem = new TCProblem();
        problem.setLink(page.getRequest().getUrl());
        page.putField("link", problem.getLink());


        List<String> vals = IntStream.range(0, 5).mapToObj(s -> "").collect(Collectors.toList());
        int valIndex = -1;
        for (Selectable node : nodes) {
            String secTitle = node.xpath("//td/h3/text()").get();
            if (StringUtils.isNotBlank(secTitle)) {
                valIndex = Arrays.asList("Problem Statement", "Definition", "Notes", "Constraints", "Examples").indexOf(secTitle.trim());
            } else {
                vals.set(valIndex,
                        vals.get(valIndex) +
                                node.xpath("//td").all()
                                        .stream()
                                        .filter(StringUtils::isNotBlank)
                                        .map(s -> s.replaceAll("^<[^<>]*>", "").replaceAll("</[^<>]*>$", ""))
                                        .map(StringEscapeUtils::unescapeHtml4)
                                        .collect(Collectors.joining())
                );
            }
        }
        problem.setStatement(vals.get(0));
        problem.setDefinition(vals.get(1));
        problem.setNotes(vals.get(2));
        problem.setConstraints(vals.get(3));
        problem.setExamples(vals.get(4));

        for (Field field : problem.getClass().getDeclaredFields()) {
            try {
                field.setAccessible(true);
                page.putField(field.getName(), field.get(problem));
            } catch (IllegalArgumentException | IllegalAccessException e) {
                logger.error(e.getLocalizedMessage(), e);
            }
        }


    }

    public static void main(String[] args) {
        System.out.println(new File("log4j.properties").getAbsolutePath());
        PropertyConfigurator.configure("log4j.properties");
        logger.info("Starting...");
        Spider.create(new ProblemCrawler())
                .addUrl("http://community.topcoder.com/stat?c=problem_statement&pm=13669&rd=16314")
                .addPipeline(new ConsolePipeline())
                .addPipeline(new TCJsonFilePipeline("data"))
                .setDownloader(new TCDowloader())
                .thread(5).run();
    }
}
