package javabasic.aop.entity;

import javabasic.aop.entity.IBusiness1;
import javabasic.aop.entity.IBusiness2;

/**
 * Created by palad on 2016/5/30.
 */
public class Business implements IBusiness1, IBusiness2 {

    @Override
    public void doBusiness1() {
        System.out.println("Invoke Business 1 in Business");
    }

    @Override
    public void doBusiness2(String arg1, String arg2) {
        System.out.println(String.format("Invoke Business 2 in Business with arg: %s, %s", arg1, arg2));
    }
}