package org.openex.tcpc.crawler;

import org.apache.commons.codec.digest.DigestUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import us.codecraft.webmagic.Page;
import us.codecraft.webmagic.Request;
import us.codecraft.webmagic.Task;
import us.codecraft.webmagic.downloader.HttpClientDownloader;
import us.codecraft.webmagic.selector.PlainText;

import java.io.IOException;

/**
 * Created by huash on 6/29/15.
 */
public class TCDowloader extends HttpClientDownloader {

    private final static Logger logger = LoggerFactory.getLogger(TCDowloader.class);

    @Override
    public Page download(Request request, Task task) {
        String pageMd5 = DigestUtils.md5Hex(request.getUrl());
        String content = null;
        try {
            content = TCFileCache.readFile(pageMd5);
        } catch (IOException e) {
            logger.info(request.getUrl() + "is not cached");
        }
        if (isContentValid(content)) {
            Page page = new Page();
            page.setRawText(content);
            page.setUrl(new PlainText(request.getUrl()));
            page.setRequest(request);
            page.setStatusCode(200);
            logger.info("get page from cache: " + request.getUrl() + " cache file: " + pageMd5);
            return page;
        } else {
            TCFileCache.removeFile(pageMd5);
        }
        Page page = null;
        try {
            logger.info("get page from URL: " + request.getUrl());
            page = super.download(request, task);
        } catch (Exception e) {
            logger.error(e.getLocalizedMessage(), e);
        }
        if (isPageValid(page)) {
            try {
                logger.info("cache " + page.getUrl() + " to " + pageMd5);
                TCFileCache.cacheFile(page.getRawText(), pageMd5);
            } catch (IOException e) {
                logger.info("cache " + request.getUrl() + " failed!!");
            }
        } else {
            logger.error("failed to download page: " + request.getUrl());
            if (page != null) {
                page.setStatusCode(404);
                logger.error(page.getRawText());
            }
        }
        return page;
    }

    private static boolean isPageValid(Page page) {
        return page != null
                && page.getStatusCode() == 200
                && isContentValid(page.getRawText());
    }

    private static boolean isContentValid(String content) {
        return content != null
                && !content.contains("Sorry, there was an error in your request.")
                && !content.contains("Problem Statement not available.");
    }

}
