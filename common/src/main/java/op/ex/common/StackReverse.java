package op.ex.common;

import java.util.Stack;

/**
 * @author huash06
 *
 *
 *	题目：用递归颠倒一个栈。例如输入栈{1, 2, 3, 4, 5}，1 在栈顶。

 */
public class StackReverse {

	public static void main(String[] args) {
		Stack<Integer> stack = new Stack<Integer>(); 
		for(int i=1; i<=5;i++){
			stack.push(i);
		}
		System.out.println(stack);
		System.out.print("  ===>\r\n    ");
		reverse(stack);
		System.out.print(stack);

	}
	
	public static void reverse(Stack<Integer> stack){
		if(stack.size()<=1){
			return;
		}
		Integer top = stack.pop();
		reverse(stack);
		putToBottom(stack,top);
	}

	private static void putToBottom(Stack<Integer> stack, Integer val) {
		if(stack.size()<=0){
			stack.push(val);
		}else{
			Integer top = stack.pop();
			putToBottom(stack, val);
			stack.push(top);
		}
		
	}

}
