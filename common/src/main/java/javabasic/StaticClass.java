package javabasic;

/**
 * Created by palad on 2016/5/30.
 */
public class StaticClass {

    // 怎么创建静态内部类和非静态内部类的实例
    public static void main(String args[]){

        // 创建静态内部类的实例
        OuterClass.NestedStaticClass printer = new OuterClass.NestedStaticClass();

        // 创建静态内部类的非静态方法
        printer.printMessage();

        // 为了创建非静态内部类，我们需要外部类的实例
        OuterClass outer = new OuterClass();
        OuterClass.InnerClass inner  = outer.new InnerClass();

        // 调用非静态内部类的非静态方法
        inner.display();

        // 我们也可以结合以上步骤，一步创建的内部类实例
        OuterClass.InnerClass innerObject = new OuterClass().new InnerClass();

        // 同样我们现在可以调用内部类方法
        innerObject.display();
    }
}

/**
 * 内部静态类不需要有指向外部类的引用。但非静态内部类需要持有对外部类的引用。

    非静态内部类能够访问外部类的静态和非静态成员。静态类不能访问外部类的非静态成员。他只能访问外部类的静态成员。

    一个非静态内部类不能脱离外部类实体被创建，一个非静态内部类可以访问外部类的数据和方法，因为他就在外部类里面。
 */
class OuterClass{
    private static String msg = "GeeksForGeeks";

    // 静态内部类
    public static class NestedStaticClass{

        // 静态内部类只能访问外部类的静态成员
        public void printMessage() {

            // 试着将msg改成非静态的，这将导致编译错误
            System.out.println("Message from nested static class: " + msg);
        }
    }

    // 非静态内部类
    public class InnerClass{

        // 不管是静态方法还是非静态方法都可以在非静态内部类中访问
        public void display(){
            System.out.println("Message from non-static nested class: "+ msg);
        }
    }
}

