package javabasic.aop;

import javabasic.aop.entity.Business;
import javassist.*;

/**
 * Created by palad on 2016/5/30.
 */
public class AopDynamicByteCodeGen {
    public static void main(String[] args) throws Exception {
        aop();
    }

    public static void aop() throws NotFoundException, CannotCompileException, InstantiationException, IllegalAccessException {
        //获取存放CtClass的容器ClassPool
        ClassPool cp = ClassPool.getDefault();

        CtClass cc = cp.get("javabasic.aop.entity.Business");
        //获得指定方法名的方法
        CtMethod m = cc.getDeclaredMethod("doBusiness1");
        //在方法执行前插入代码
        m.insertBefore("{ System.out.println(\"Log before doBusiness1\"); }");
        ((Business)cc.toClass().newInstance()).doBusiness1();

    }
}
