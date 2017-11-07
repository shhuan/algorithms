package ex.topcoder.challenge;

/**
 * Created by huash06 on 7/2/2015.
 */

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.apache.commons.lang3.StringUtils;
import org.apache.log4j.PropertyConfigurator;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.client.RestTemplate;

import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

@SpringBootApplication
public class App implements CommandLineRunner {

    private static final Logger log = LoggerFactory.getLogger(App.class);

    public static void main(String args[]) {
        SpringApplication.run(App.class);
    }

    @Override
    public void run(String... strings) {
        log.info("Starting App");
        PropertyConfigurator.configure("log4j.properties");
        RestTemplate restTemplate = new RestTemplate();
        String quote = restTemplate.getForObject("http://gturnquist-quoters.cfapps.io/api/random", String.class);
        log.info(quote);

        String ak = "D3e72e98aed50ac9b3a417853efff59e";

        List<Place> places = new ArrayList<>();
        Gson gson = new GsonBuilder().disableHtmlEscaping().setPrettyPrinting().create();

        IntStream.range(0, 20).forEach(pageIndex -> {
            String url = "http://api.map.baidu.com/place/v2/search?ak=" + ak + "&output=json&query=%E5%8C%BB%E9%99%A2" +
                    "&page_size=20&page_num=" + pageIndex + "&scope=2&region=%E5%8C%97%E4%BA%AC";

            String placeList = HttpHelper.getResponse(url);
            AtomicInteger index = new AtomicInteger(0);
            if (StringUtils.isNotBlank(placeList)) {
                PlaceResponse resp = gson.fromJson(placeList, PlaceResponse.class);
                log.info(resp.toString());
                places.addAll(
                        resp.getResults().stream()
                                .filter(p -> StringUtils.isNotBlank(p.getDetail_info().getDetail_url()))
                                .map(p -> {
                                    String purl = p.getDetail_info().getDetail_url();
                                    try {
                                        log.info("Getting image from " + purl);
                                        Document doc = Jsoup.connect(purl).userAgent(
                                                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36")
                                                .get();
                                        Elements imgs =
                                                doc.select(
                                                        "#basicInfo > div.bd.clearfix > div.meta.meta-img > a > img");
                                        String imageUrl =
                                                imgs.stream().filter(i -> StringUtils.isNotBlank(i.attr("src")))
                                                        .findAny()
                                                        .map(i -> i.attr("src")).get();
                                        log.info("Found image " + imageUrl);
                                        p.getDetail_info().setImage_url(imageUrl);
                                    } catch (Exception e) {
                                        log.error(e.getLocalizedMessage(), e);
                                    }
                                    return p;
                                }).filter(p -> StringUtils.isNotBlank(p.getDetail_info().getImage_url()))
                                .filter(p -> {
                                    try {
                                        downloadImage(p.getDetail_info().getImage_url(),
                                                "result/" + p.getName() + ".jpg");
                                        return true;
                                    } catch (Exception e) {
                                        e.printStackTrace();
                                    }
                                    return false;
                                }).collect(Collectors.toList())
                );
            }
        });

        try (BufferedWriter writer = Files.newBufferedWriter(Paths.get("result/list.json"))) {
            gson.toJson(places.stream()
                    .filter(p -> Files.exists(Paths.get("result/" + p.getName() + ".jpg")))
                    .collect(Collectors.toList()), writer);
        } catch (Exception e) {
            log.error(e.getLocalizedMessage(), e);
        }

    }

    public static void downloadImage(String sourceUrl, String path)
            throws MalformedURLException, IOException, FileNotFoundException {
        if (Files.exists(Paths.get(path))) {
            log.info(path + " exists, skip download");
            return;
        }
        URL imageUrl = new URL(sourceUrl);
        try (InputStream imageReader = new BufferedInputStream(
                imageUrl.openStream());
             OutputStream imageWriter = new BufferedOutputStream(
                     new FileOutputStream(path))) {
            int readByte;

            while ((readByte = imageReader.read()) != -1) {
                imageWriter.write(readByte);
            }
        }
    }


}