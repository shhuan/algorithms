package op.ex.common;

/**
 * @author huash06
 *
 *
 *		数组中超过出现次数超过一半的数字
		题目：数组中有一个数字出现的次数超过了数组长度的一半，找出这个数字。
		分析：这是一道广为流传的面试题，包括百度、微软和Google 在内的多家公司都
		曾经采用过这个题目。要几十分钟的时间里很好地解答这道题，
		除了较好的编程能力之外，还需要较快的反应和较强的逻辑思维能力。
		
		
		两两删除两个不同的数字，最后剩下的就是结果
 */
public class NumberAppearsOverHalf {

	public static void main(String[] args) {
		System.out.println(getMajor(new int[]{1,2,1,1,1,2,3,4,2,3,1}));

	}
	
	public static int getMajor(int[] A){
		int x=A[0];
		int count = 1;
		for(int i=1; i<A.length; i++){
			if(count==0){
				x = A[i];
				count++;
			}else if(A[i]==x){
				count++;
			}else{
				count--;
			}
		}
		return x;
	}

}
