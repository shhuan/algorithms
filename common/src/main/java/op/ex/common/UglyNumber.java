package op.ex.common;

import java.util.PriorityQueue;
import java.util.Queue;

/**
 * @author huash06
 *
 *
 *		寻找丑数。
		题目：我们把只包含因子2、3 和5 的数称作丑数（Ugly Number）。例如6、8 都是丑数，
		但14 不是，因为它包含因子7。习惯上我们把1 当做是第一个丑数。求按从小到大的顺序的第1500 个丑数。
		
		
		
		使用优先级队列
 */
public class UglyNumber {

	public static void main(String[] args) {
		search();

	}
	
	public static void search(){
		Queue<Integer> q = new PriorityQueue<>();
		int[] mul = new int[]{2,3,5};
		q.add(2);
		q.add(3);
		q.add(5);
		for(int i=0; i<1500;i++){
			Integer val = q.poll();
			System.out.println(val);
			for(int j=0; j<mul.length; j++){
				int nv = val*mul[j];
				if(!q.contains(nv)){
					q.add(nv);
				}
			}
			i++;
		}
	}

}
