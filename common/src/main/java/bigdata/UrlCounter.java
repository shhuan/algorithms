package bigdata;

import com.sun.xml.internal.ws.api.ha.StickyFeature;

import java.io.*;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;
import java.util.stream.IntStream;

/**
 * Created by huash on 2015/8/10.
 */
public class UrlCounter {




    public static void main(String[] args){

        try {
            count("urls.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static int subFileCount = 0;
    public static void count(String fileName) throws IOException {

        split(fileName);
    }

    private static int MAXSIZE = 100_000_000;
    private static int MAX_FILE_SIZE = 10_000_000;
//    private static Map<Integer, Integer> hashFileIndice = new HashMap<>();
    public static void split(String fileName) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(fileName));
        Integer[] counts = new Integer[2*MAXSIZE];
        Arrays.fill(counts, 0);
        reader.lines().forEach(url -> {
            Integer hash = hashUrl(url);
            counts[hash]++;
        });

        System.out.println("Finished count hash ");

        int[] fileSize = new int[100];
        Arrays.fill(fileSize, 0);
        subFileCount = 0;
        int[] hashFileIndice = new int[2*MAXSIZE];
        Arrays.fill(hashFileIndice, 0);

        IntStream.range(0, counts.length).filter(i->counts[i]>0).forEach(i->{
            fileSize[subFileCount] += counts[i];
            if (fileSize[subFileCount] > MAX_FILE_SIZE){
                subFileCount ++;
            }
            hashFileIndice[i] = subFileCount;
        });
        subFileCount++;
        System.out.println("Finished count subfile "+subFileCount);

        List<BufferedWriter> writers = new ArrayList<>();
        for (int i = 0; i < subFileCount; i++) {
            writers.add(new BufferedWriter(new FileWriter(subFileName(i))));
        }
        reader.close();
        reader = new BufferedReader(new FileReader(fileName));
        reader.lines().parallel().forEach(url -> {
            int hash = hashUrl(url);
            int fi = hashFileIndice[hash];
            try {
                writers.get(fi).write(url + "\r\n");
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        for (BufferedWriter writer : writers){
            writer.flush();
            writer.close();
        }
        reader.close();

        System.out.println("Finished spliting files");

        List<BufferedReader> readers = new ArrayList<>();
        for (int i = 0; i < subFileCount; i++) {
            readers.add(new BufferedReader(new FileReader(subFileName(i))));
        }

        BufferedWriter writer = new BufferedWriter(new FileWriter("result.txt"));
        Map<String, Integer> sc = new HashMap<>();
        readers.forEach(r -> {
            r.lines().forEach(url -> {
                Integer c = sc.get(url);
                c = c == null ? 0 : c;
                sc.put(url, c + 1);
            });
            for (String url : sc.keySet()) {
                try {
                    writer.write(url + " " + sc.get(url) + "\r\n");
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("Finished counting urls in "+r.toString());
            sc.clear();
            try {
                writer.flush();
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
        writer.flush();
        writer.close();
        System.out.println("Finished merge");

        for (BufferedReader r : readers){
            r.close();
        }

    }

    private static String subFileName(int index){
        return "sub_"+index+".txt";
    }
    private static String subResultFileName(int index){
        return "result_"+index+".txt";
    }

    public static int hashUrl(String url){
        return MAXSIZE+url.hashCode() % MAXSIZE;
    }

    public static void serializeCount(Map<String, Integer> counts) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter("sf_"+subFileCount+".txt"));
        for (String key : counts.keySet()){
            writer.write(key+" "+counts.get(key));
        }
        writer.close();
        subFileCount++;
        counts.clear();
    }

    public static void mergeCount() throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter("result.txt"));

        Map<String, Integer> counts = new TreeMap<>();

        List<BufferedReader> readers = new ArrayList<>();
        for (int i = 0; i < subFileCount; i++) {
            readers.add(new BufferedReader(new FileReader(("sf_"+i+".txt"))));
        }

        int currentFile = 0;






        writer.close();
    }


}
