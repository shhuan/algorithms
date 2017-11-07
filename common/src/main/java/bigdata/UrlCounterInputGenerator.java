package bigdata;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

/**
 * Created by huash on 2015/8/10.
 */
public class UrlCounterInputGenerator {

    public static void main(String[] args){


        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(new File("urls.txt")));
//            int count = 100_000_000;
            int count = 100_000;
            Map<String, Integer> urls = generateUrl(count, 100);
            int c = 0;

            Set<String> keySet = urls.keySet();
            Map<Integer, String> ik = new HashMap<>();
            int ki = 0;
            for (String key : keySet) {
                ik.put(ki++, key);
            }

            while (!ik.isEmpty()){
                int i = rand.nextInt(ik.size());
                System.out.println(i);
                String url = ik.get(i);
                if (urls.get(url) > 0){
                    urls.put(url, urls.get(url)-1);
                    c ++;
                    writer.write(url+"\r\n");
                }else {
                    ik.remove(i);
                }
            }
            writer.flush();
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static Map<String, Integer> generateUrl(int count, int maxRepeat){
        Map<String, Integer> result = new HashMap<>();
        int c = 0;
        while (c < count){
            String url = generateUrl();
            int r = rand.nextInt(maxRepeat)+1;
            c += r;
            if (c > count){
                r -= c-count;
            }
            result.put(url, r);
        }
        return result;
    }
    private static Random rand = new Random();
    public static String generateUrl(){

        int parts = rand.nextInt(10)+1;
        StringBuilder url = new StringBuilder();

        for (int i = 0; i < parts; i++) {
            StringBuilder part = new StringBuilder();
            int len = rand.nextInt(10)+1;
            for (int j = 0; j < len; j++) {
                part.append((char)(rand.nextInt(26)+(int)('a')));
            }
            url.append(part.toString());
            url.append("/");
        }


        int pi = rand.nextInt(5);
        String protocol = "";
        switch (pi){
            case 0:
                protocol = "http://";
                break;
            case 1:
                protocol = "https://";
                break;
            case 2:
                protocol = "ftp://";
                break;
            default:
                protocol = "www.";
                break;
        }

        if (url.length() > 20){
            return protocol+url.substring(0, 20);
        }
        return protocol+url.toString();
    }
}
