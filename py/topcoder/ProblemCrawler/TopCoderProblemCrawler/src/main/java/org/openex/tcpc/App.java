package org.openex.tcpc;
import org.apache.log4j.PropertyConfigurator;
import org.openex.tcpc.crawler.ArchiveCrawler;
import org.openex.tcpc.crawler.TCDowloader;
import org.openex.tcpc.crawler.TCJsonFilePipeline;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import us.codecraft.webmagic.Spider;
import us.codecraft.webmagic.pipeline.ConsolePipeline;

import java.io.File;


public class App {

    private static final Logger logger = LoggerFactory.getLogger(App.class);

    public static void main(String[] args) {

        System.out.println(App.class.getResource("/").getPath());
        System.out.println(new File("log4j.properties").getAbsolutePath());
        PropertyConfigurator.configure("log4j.properties");
        logger.info("Starting...");
        Spider.create(new ArchiveCrawler())
                .addUrl("http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=1")
                .addUrl("http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=201")
                .addUrl("http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=401")
                .addUrl("http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=601")
                .addUrl("http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=801")
                .addPipeline(new ConsolePipeline())
                .addPipeline(new TCJsonFilePipeline("data"))
                .setDownloader(new TCDowloader())
                .thread(5).run();
    }
}
