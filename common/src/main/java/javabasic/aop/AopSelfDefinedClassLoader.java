package javabasic.aop;

import javabasic.aop.entity.Business;
import javassist.*;

/**
 * Created by palad on 2016/5/30.
 *
 * 自定义的类加载器实现AOP只能拦截使用这个加载器加载的字节码
 */
public class AopSelfDefinedClassLoader {

    public static void main(String[] args) throws Exception {
        aop();
    }

    public static void aop() throws NotFoundException, CannotCompileException, InstantiationException, IllegalAccessException {
        //获取存放CtClass的容器ClassPool
        ClassPool cp = ClassPool.getDefault();
        //创建一个类加载器
        Loader cl = new Loader();
        //增加一个转换器，让类加载的时候
        cl.addTranslator(cp, new MyTranslator());
        //将类装载到JVM
        try {
            cl.run("javabasic.aop.AopSelfDefinedClassLoader$MyTranslator", null);
        } catch (Throwable e) {
            e.printStackTrace();
        }

    }

    public static class MyTranslator implements Translator {

        public void start(ClassPool pool) throws NotFoundException, CannotCompileException {
        }

        /* *
         * 类装载到JVM前进行代码织入
         */
        public void onLoad(ClassPool pool, String classname) {
            if (!"javabasic.aop.entity.Business".equals(classname)) {
                return;
            }
            //通过报名获取类文件
            try {
                CtClass cc = pool.get(classname);
                //获得指定方法名的方法
                CtMethod m = cc.getDeclaredMethod("doBusiness2");
                //在方法执行前插入代码
                m.insertBefore("{ System.out.println(\"Log before method\"); }");

                m.insertAfter("{ System.out.println(\"Log after method\" );}");
            } catch (NotFoundException e) {
            } catch (CannotCompileException e) {
            }
        }

        public static void main(String[] args) {
            Business b = new Business();
            b.doBusiness2("arg1", "arg2");
            b.doBusiness1();
        }
    }
}


