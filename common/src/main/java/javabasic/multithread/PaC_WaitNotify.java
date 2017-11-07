package javabasic.multithread;

import java.util.LinkedList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Created by huash on 2016/6/1.
 */
public class PaC_WaitNotify {

    public static void main(String[] args) {
        Storage storage = new Storage();

        ExecutorService executorService = Executors.newFixedThreadPool(10);
        for (int i = 0; i < 9; i++) {
            // 超过一个生产者线程的时候,仓库会溢出。
            // 是因为可能生产者notify之后唤醒的是另外一个wait的生产者
            // 可以在wait之后再加一次判断
            Producer producer = new Producer(storage);
            executorService.submit(producer);
        }
        executorService.submit(new Consumer(storage));
    }
}



class Producer extends Thread{

    private Storage storage;
    private static AtomicInteger atomicInteger = new AtomicInteger(0);
    public Producer(Storage storage) {
        this.storage = storage;
    }

    @Override
    public void run() {
        while (true) {
            synchronized (storage) {
                try {
                    if (storage.size() >= Storage.MAX_SIZE) {
                        System.out.println("Storage is full, waiting...");
                        storage.wait();
                    }

                    if (storage.size() >= Storage.MAX_SIZE) {
                        continue;
                    }
                    String product = "Product " + currentThread().getName() + " " + atomicInteger.incrementAndGet();
                    storage.add(product);
                    System.out.println("Produce " + product);
                    storage.notify();
                    sleep(new Random().nextInt(100));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

class Consumer extends Thread{
    private Storage storage;
    public Consumer(Storage storage) {
        this.storage = storage;
    }

    @Override
    public void run() {
        while (true) {
            synchronized (storage) {
                try {
                    if (storage.size() <= 0) {
                        System.out.println("Storage is empty, waiting...");
                        storage.wait();
                    }
                    System.out.println("Consume " + storage.remove());
                    storage.notify();
                    sleep(new Random().nextInt(100));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

class Storage {
    public static final int MAX_SIZE = 5;

    List<String> repo = new LinkedList<>();

    public int size() {
        return repo.size();
    }

    public void add(String p) {
        if (repo.size() >= MAX_SIZE) {
            System.out.println("repository is full, ignore " + p);
        } else {
            repo.add(p);
        }
    }

    public String remove() {
        if (repo.isEmpty()) {
            System.out.println("repository is empty!");
            return null;
        }
        return repo.remove(0);
    }
}