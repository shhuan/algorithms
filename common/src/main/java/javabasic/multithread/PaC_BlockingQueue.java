package javabasic.multithread;

import java.util.Random;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

/**
 * Created by huash on 2016/6/15.
 */
public class PaC_BlockingQueue {
    public static void main(String args[]){

        //Creating shared object
        BlockingQueue<String> sharedQueue = new LinkedBlockingQueue<>();

        // 最多创建M个产品，最多消费N个产品
        final int M = 15;
        final int N = 10;

        // PC个创建者线程，CC个消费者线程
        final int PC = 3;
        final int CC = 2;

        ExecutorService executorService = Executors.newFixedThreadPool(PC+CC);

        AtomicInteger consumed = new AtomicInteger(0);
        AtomicInteger produced = new AtomicInteger(0);
        IntStream.range(0, PC).forEach(i -> executorService.submit(new Producer(sharedQueue, produced, M)));
        IntStream.range(0, CC).forEach(i -> executorService.submit(new Consumer(sharedQueue, consumed, N)));

        try {
            executorService.awaitTermination(5, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static class Producer extends Thread {

        private final BlockingQueue sharedQueue;
        private AtomicInteger produced;
        private int count;
        public Producer(BlockingQueue sharedQueue, AtomicInteger produced, int count) {
            this.sharedQueue = sharedQueue;
            this.produced = produced;
            this.count = count;
        }

        @Override
        public void run() {
            for(;;){
                try {
                    sleep(new Random().nextInt(1000) + 10);
                } catch (InterruptedException e) {
                    System.out.println(e.getLocalizedMessage());
                }

                int pi = produced.incrementAndGet();
                if (pi > count) {
                    break;
                }
                String product = "Product-" + pi;
                System.out.println(String.format("%s Produced : %s", getName(), product));
                try {
                    sharedQueue.put(product);
                } catch (InterruptedException e) {
                    produced.decrementAndGet();
                    e.printStackTrace();
                }
            }
            System.out.println("Producer " + getName() + "finished");
        }

    }

    public static class Consumer extends Thread{

        private final BlockingQueue sharedQueue;
        private AtomicInteger consumed;
        private int count;
        public Consumer (BlockingQueue sharedQueue, AtomicInteger consumed, int count) {
            this.sharedQueue = sharedQueue;
            this.consumed = consumed;
            this.count = count;
        }

        @Override
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
                    System.out.println(String.format("%s Consumed : %s", this.getName(), sharedQueue.take()));
                } catch (InterruptedException e) {
                    consumed.decrementAndGet();
                    e.printStackTrace();
                }
            }
            System.out.println("Consumer " + getName() + " finished");
        }

    }
}


