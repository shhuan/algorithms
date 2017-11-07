package javabasic.multithread;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

/**
 * Created by huash on 2016/6/14.
 */
public class PaC_Semaphore {

    public static void main(String args[]) {
        // 最多创建M个产品，最多消费N个产品
        final int M = 15;
        final int N = 10;

        // PC个创建者线程，CC个消费者线程
        final int PC = 3;
        final int CC = 2;

        Semaphore semaphore = new Semaphore(1);
        Store<String> store = new Store<>();

        ExecutorService executorService = Executors.newFixedThreadPool(PC+CC);

        IntStream.range(0, PC).forEach(i -> executorService.submit(new Producer(semaphore, store, M)));
        IntStream.range(0, CC).forEach(i -> executorService.submit(new Consumer(semaphore, store, N)));

        try {
            executorService.awaitTermination(5, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    /**
     * Producer Class.
     */
    public static class Producer extends Thread{

        Semaphore semaphore;
        Store<String> store;
        int count;
        public static AtomicInteger prodSeq = new AtomicInteger(0);

        public Producer(Semaphore semaphore, Store<String> store, int count) {
            this.semaphore = semaphore;
            this.store = store;
            this.count = count;
        }

        public void run() {
            while (true) {
                try {
                    sleep(new Random().nextInt(1000) + 10);
                } catch (InterruptedException e) {
                    System.out.println(e.getLocalizedMessage());
                }
                int pi = prodSeq.incrementAndGet();
                if (pi > count) {
                    break;
                }
                String product = "Product-" + pi;
                System.out.println(String.format("%s Produced : %s", getName(), product));
                this.store.add(product);
                semaphore.release();
            }

            System.out.println("Producer " + getName() + "finished");
        }
    }

    /**
     * Consumer Class.
     */
    public static class Consumer extends Thread{

        Semaphore semaphore;
        Store<String> store;
        int count;
        public static AtomicInteger consumed = new AtomicInteger(0);

        public Consumer(Semaphore semaphore, Store<String> store, int count) {
            this.semaphore = semaphore;
            this.store = store;
            this.count = count;
        }

        public void run() {
            while(true) {
                try {
                    sleep(new Random().nextInt(1000) + 20);
                } catch (InterruptedException e) {
                    System.out.println(e.getLocalizedMessage());
                }
                if (consumed.incrementAndGet() > count) {
                    break;
                }
                try {
                    semaphore.acquire();
                    System.out.println(String.format("%s Consumed : %s", this.getName(), store.get()));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("Consumer " + getName() + " finished");
        }

    }
}
