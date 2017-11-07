package javabasic.multithread;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by huash on 2016/6/15.
 */
public class Store<T> {
    List<T> repo = new ArrayList<>();

    synchronized public T get() {
        return repo.remove(0);
    }

    synchronized public void add(T p) {
        repo.add(p);
    }
}
