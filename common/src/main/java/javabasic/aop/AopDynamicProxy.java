package javabasic.aop;

import javabasic.aop.entity.IBusiness1;
import javabasic.aop.entity.IBusiness2;
import javabasic.aop.entity.Business;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

/**
 * Created by palad on 2016/5/30.
 *
 * 代理类必须实现接口，没实现接口会抛出异常
 * 反射机制对性能有影响
 * 字节码加载后会存放在JVM运行时的方法区（持久代）中，大量使用动态代理时可能会引起FULL GC，可以把持久代设置大一些
 */
public class AopDynamicProxy {

    public static void main(String[] args) {
        //需要代理的接口，被代理类实现的多个接口都必须在这里定义
        Class[] proxyInterface = new Class[] { IBusiness1.class, IBusiness2.class };
        //构建AOP的Advice，这里需要传入业务类的实例
        LogInvocationHandler handler = new LogInvocationHandler(new Business());
        //生成代理类的字节码加载器
        ClassLoader classLoader = AopDynamicProxy.class.getClassLoader();
        //织入器，织入代码并生成代理类
        IBusiness2 proxyBusiness = (IBusiness2) Proxy.newProxyInstance(classLoader, proxyInterface, handler);
        //使用代理类的实例来调用方法。
        proxyBusiness.doBusiness2("arg1", "arg2");
        ((IBusiness1) proxyBusiness).doBusiness1();
    }
}

class LogInvocationHandler implements InvocationHandler {
    private Object target;

    LogInvocationHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        if (method.getName().equals("doBusiness2")) {
            System.out.println("Log before doBusiness2");
        }
        //执行原有逻辑
        Object rev = method.invoke(target, args);
        //执行织入的日志，你可以控制哪些方法执行切入逻辑
        if (method.getName().equals("doBusiness2")) {
            System.out.println("Log after doBusiness2");
        }
        return rev;
    }
}