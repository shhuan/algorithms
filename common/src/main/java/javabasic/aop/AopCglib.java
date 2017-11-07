package javabasic.aop;

import java.lang.reflect.Method;

import javabasic.aop.entity.Business;
import javabasic.aop.entity.IBusiness2;
import net.sf.cglib.proxy.*;

/**
 * Created by palad on 2016/5/30.
 * 使用动态字节码生成技术实现AOP原理是在运行期间目标字节码加载后，生成目标类的子类，将切面逻辑加入到子类中，所以使用Cglib实现AOP不需要基于接口。
 * Cglib封装了ASM
 * 可以运行期扩展Java类和实现Java接口
 *
 */
public class AopCglib {

    public static void main(String[] args) {
        byteCodeGe();
    }

    public static void byteCodeGe() {
        //创建一个织入器
        Enhancer enhancer = new Enhancer();
        //设置父类
        enhancer.setSuperclass(Business.class);
        //设置需要织入的逻辑
        enhancer.setCallback(new LogIntercept());
        //使用织入器创建子类
        IBusiness2 newBusiness = (IBusiness2) enhancer.create();
        newBusiness.doBusiness2("arg1", "arg2");
    }

    /**
     * 记录日志
     */
    public static class LogIntercept implements MethodInterceptor {

        @Override
        public Object intercept(Object target, Method method, Object[] args, MethodProxy proxy) throws Throwable {
            if (method.getName().equals("doBusiness2")) {
                System.out.println("Log before doBusiness2");
            }

            //执行原有逻辑，注意这里是invokeSuper
            Object rev = proxy.invokeSuper(target, args);
            //执行织入的日志
            if (method.getName().equals("doBusiness2")) {
                System.out.println("Log after doBusiness2");
            }
            return rev;
        }
    }
}

