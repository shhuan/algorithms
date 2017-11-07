package op.ex.common;

import java.util.Arrays;
import java.util.Comparator;

/**
 * @author huash06
 *
 *
 *	把数组排成最小的数。
	题目：输入一个正整数数组，将它们连接起来排成一个数，输出能排出的所有数字中最小的
	一个。
	例如输入数组{32, 321}，则输出这两个能排成的最小数字32132。
	请给出解决问题的算法，并证明该算法。
	
	如果ab<ba,那么a排在b的前面
 */
public class ComposeMinNumber {

	public static void main(String[] args) {
		System.out.println(smallestDigit(new int[]{32,321}));

	}
	
	public static String smallestDigit(int a[]) {
	  Integer aux[] = new Integer[a.length];
	  for (int i=0; i<a.length; i++) aux[i] = a[i];
	  Arrays.sort(aux, new Comparator<Integer>(){
		@Override
		public int compare(Integer i1, Integer i2) {
		      return (""+i1+i2).compareTo(""+i2+i1);
		}
	  });
	  StringBuffer sb = new StringBuffer();
	  for (int i=0; i<aux.length; i++) {
	    sb.append(aux[i]);
	  }
	  return sb.toString();
	}

}
