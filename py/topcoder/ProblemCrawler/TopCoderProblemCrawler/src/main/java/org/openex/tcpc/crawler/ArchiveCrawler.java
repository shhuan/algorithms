package org.openex.tcpc.crawler;

import org.openex.tcpc.bean.TCMatch;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import us.codecraft.webmagic.Page;
import us.codecraft.webmagic.Spider;
import us.codecraft.webmagic.pipeline.ConsolePipeline;
import us.codecraft.webmagic.selector.Selectable;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ArchiveCrawler extends BasicCrawler{

    private final static Logger logger = LoggerFactory.getLogger(ArchiveCrawler.class);

    @Override
	public void process(Page page) {
        if (!isValidPage(page)){
            logger.error("page is invalid: "+page.getRequest().getUrl());
            return;
        }
		logger.info("Processing Archive {}", page.getRequest().getUrl());
		List<Selectable> matchNodes = page.getHtml().css("body > table > tbody > tr > td.statTableSpacer > form > table > tbody > tr:nth-child(n+5)").nodes();
		List<TCMatch> matches = new ArrayList<>();
		matchNodes.stream().forEach(node -> {
			try{
				List<String> tds = node.xpath("td/text()").all();
				TCMatch match = new TCMatch();
				tds = tds.stream().map(s -> {
					if(s.trim().replaceAll("\\s", "").equals("")){
						return "0";
					}
					return s;
				}).collect(Collectors.toList());
				
				match.setTime(tds.get(1));
				match.setCompetitorsTotal(Integer.parseInt(tds.get(2)));
				match.setCompetitorsDiv1(Integer.parseInt(tds.get(3)));
				match.setCompetitorsDiv2(Integer.parseInt(tds.get(4)));
				match.setSubmissionTotalDiv1(Integer.parseInt(tds.get(5)));
				match.setSubmissionAvgDiv1(Float.parseFloat(tds.get(6)));
				match.setChallengeTotalDiv1(Integer.parseInt(tds.get(7)));
				match.setChallengeAvgDiv1(Float.parseFloat(tds.get(8)));
				match.setSubmissionTotalDiv2(Integer.parseInt(tds.get(9)));
				match.setSubmissionAvgDiv2(Float.parseFloat(tds.get(10)));
				match.setChallengeTotalDiv2(Integer.parseInt(tds.get(11)));
				match.setChallengeAvgDiv2(Float.parseFloat(tds.get(12)));
				match.setName(node.xpath("td/a/text()").get());
				match.setLink(node.links().get());

				Spider.create(new MatchCrawler())
						.addUrl(match.getLink())
						.addPipeline(new ConsolePipeline())
						.addPipeline(new TCJsonFilePipeline("data/matches"))
						.setDownloader(new TCDowloader())
						.thread(5)
						.run();

				matches.add(match);
			}catch (RuntimeException e){
				logger.error("Error while parsing {}", node.get());
				logger.error(e.getLocalizedMessage(), e);
			}
		});
		page.putField("matches", matches);
		
	}

	public static void main(String[] args) {
        Spider.create(new ArchiveCrawler())
        	.addUrl("http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=1")
        	.addUrl("http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=201")
        	.addUrl("http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=401")
        	.addUrl("http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=601")
        	.addUrl("http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=801")
        	.addPipeline(new ConsolePipeline())
        	.addPipeline(new TCJsonFilePipeline("data"))
        	.thread(5).run();
	}

}
