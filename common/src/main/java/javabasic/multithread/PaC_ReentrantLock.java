package javabasic.multithread;

import java.util.Random;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.stream.IntStream;

/**
 * Created by huash on 2016/6/15.
 */
public class PaC_ReentrantLock {
    public static void main(String[] args) {
        // 最多创建M个产品，最多消费N个产品
        final int M = 15;
        final int N = 10;

        // PC个创建者线程，CC个消费者线程
        final int PC = 3;
        final int CC = 2;

        BoundedBuffer buffer = new BoundedBuffer();
        ExecutorService executorService = Executors.newFixedThreadPool(PC+CC);

        AtomicInteger consumed = new AtomicInteger(0);
        AtomicInteger produced = new AtomicInteger(0);
        IntStream.range(0, PC).forEach(i -> executorService.submit(new Producer(buffer, produced, M)));
        IntStream.range(0, CC).forEach(i -> executorService.submit(new Consumer(buffer, consumed, N)));
    }

    /***
     * The following code is taken from the JavaDoc of Condition:
     * http://docs.oracle.com/javase/1.5.0/docs/api/java/util/concurrent/locks/Condition.html
     *
     * 在PaC_WaitNotify中，使用Object的wait和notify方法。当生产者和消费者同时因wait方法挂起后，调用notify方法
     * 不能够确定被唤醒的是哪个线程。
     *
     * 使用条件可以
     */
    public static class BoundedBuffer {
        final Lock lock = new ReentrantLock();

        final Condition notFull  = lock.newCondition();
        final Condition notEmpty = lock.newCondition();

        final Object[] items = new Object[100];
        int putptr, takeptr, count;

        public void put(Object x) throws InterruptedException {
            lock.lock();
            try {
                while (count == items.length)
                    notFull.await();
                items[putptr] = x;
                if (++putptr == items.length) putptr = 0;
                ++count;
                notEmpty.signal();
            } finally {
                lock.unlock();
            }
        }

        public Object take() throws InterruptedException {
            lock.lock();
            try {
                while (count == 0)
                    notEmpty.await();
                Object x = items[takeptr];
                if (++takeptr == items.length) takeptr = 0;
                --count;
                notFull.signal();
                return x;
            } finally {
                lock.unlock();
            }
        }
    }

    public static class Producer extends Thread {

        private final BoundedBuffer buffer;
        private AtomicInteger produced;
        private int count;
        public Producer(BoundedBuffer buffer, AtomicInteger produced, int count) {
            this.buffer = buffer;
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
                    buffer.put(product);
                } catch (InterruptedException e) {
                    produced.decrementAndGet();
                    e.printStackTrace();
                }
            }
            System.out.println("Producer " + getName() + "finished");
        }

    }

    public static class Consumer extends Thread{

        private final BoundedBuffer buffer;
        private AtomicInteger consumed;
        private int count;
        public Consumer (BoundedBuffer buffer, AtomicInteger consumed, int count) {
            this.buffer = buffer;
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
                    System.out.println(String.format("%s Consumed : %s", this.getName(), buffer.take().toString()));
                } catch (InterruptedException e) {
                    consumed.decrementAndGet();
                    e.printStackTrace();
                }
            }
            System.out.println("Consumer " + getName() + " finished");
        }

    }
}
