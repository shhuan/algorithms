package org.openex.tcpc.crawler;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.util.stream.Collectors;

/**
 * Created by huash on 6/29/15.
 */
public class TCFileCache {

    private final static Logger logger = LoggerFactory.getLogger(TCFileCache.class);
    final private static String FOLDER = "data/cache";

    public static void cacheFile(String content, String fileName) throws IOException {
        Path path = FileSystems.getDefault().getPath(FOLDER, fileName);
        Files.write(path, content.getBytes());
        logger.info("Cached file "+ fileName);
    }

    public static String readFile(String fileName) throws IOException {
        return Files.lines(FileSystems.getDefault().getPath("data/cache", fileName)).collect(Collectors.joining());
    }

    public static void removeFile(String pageMd5) {
        try {
            Files.delete(FileSystems.getDefault().getPath(FOLDER, pageMd5));
        } catch (NoSuchFileException ne) {
            logger.info(pageMd5 + " doesn't exist, no need to delete");
        } catch (IOException e) {
            logger.error("error while removing cache: " + e.getLocalizedMessage(), e);
        }
    }
}
