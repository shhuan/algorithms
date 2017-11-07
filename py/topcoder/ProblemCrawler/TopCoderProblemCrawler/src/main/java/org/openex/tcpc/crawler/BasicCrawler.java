package org.openex.tcpc.crawler;

import com.google.common.collect.Sets;
import org.apache.commons.lang3.StringUtils;
import us.codecraft.webmagic.Page;
import us.codecraft.webmagic.Site;
import us.codecraft.webmagic.processor.PageProcessor;

/**
 * Created by huash on 6/29/15.
 */
public class BasicCrawler implements PageProcessor {

    final private Site site = Site.me().setAcceptStatCode(Sets.newHashSet(200)).setTimeOut(1000).setRetryTimes(3).setSleepTime(1000);

    public boolean isValidPage(Page page) {
        return page.getStatusCode() == 200
                && StringUtils.isNotBlank(page.getRawText())
                && !page.getRawText().contains("Sorry, there was an error in your request.");
    }

    @Override
    public void process(Page page) {
    }

    @Override
    public Site getSite() {
        return site;
    }
}
