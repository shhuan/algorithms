package open.ex.amzaon;

import java.util.Scanner;

/*
 * 
 * Question 1 / 2.
 Given an array A, find the maximum neighboring-peak-valley difference of A,  MaxD(A).

 For example, A={2, 3, 6, 5, 7, 9}, the elements 2, 5 could be regarded as the valley while 6 and 9 are the peaks.
 The difference of each neighboring peak-valley pair could be enumerated as below:
 D[2, 6]=4, D[6,5]=1, D=[5,9]=4.
 Thus, MaxD(A)=4.

 Please write a program to find the maximum neighboring-peak-valley difference of an array.
 The input contains several lines(10 lines at most), and each line contains of several numbers 
 separated by space. We treat every line an array.And each line has 2 numbers at least and 20 numbers at most.

 The output should be the maximum neighboring-peak-valley difference of the arrays and separated by comma. For example:

 Input:
 2 3 6 5 7 9
 2 3 6 5 7
 2 3 6 5 7 9 10

 Output:
 4,4,5
 * 
 */
public class MaxNeighborPeakValley_Easy {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		while(sc.hasNextLine()){
			String[] valsStr = sc.nextLine().split(" ");
			int[] vals = new int[valsStr.length];
			for(int i=0; i<valsStr.length; i++){
				vals[i] = Integer.valueOf(valsStr[i]);
			}
			if(sb.length()>0){
				sb.append(",");
			}
			sb.append(maxD(vals));
		}
		sc.close();
		System.out.println(sb.toString());
		
	}
	
	
	public static int maxD(int[] vals){
		int maxd = -1;
		int preVal = Integer.MIN_VALUE;
		for(int i=0; i<vals.length; i++){
			if(isValley(vals,i) || isPeak(vals,i)){
				if(preVal==Integer.MIN_VALUE){
					preVal = vals[i];
				}else{
					int td = Math.abs(vals[i]-preVal);
					maxd = td>maxd?td:maxd;
					preVal = vals[i];
				}
			}
		}
		return maxd;
	}
	
	
	private static boolean isValley(int[] vals, int index){
		if(index==0 && vals[1]>vals[0]){
			return true;
		}else if(index==vals.length-1 && vals[index-1]>vals[index]){
			return true;
		}else if(index>0 && index<vals.length-1){
			return vals[index-1]>vals[index] && vals[index+1]>vals[index];
		}
		return false;
	}
	private static boolean isPeak(int[] vals, int index){
		if(index==0 && vals[1]<vals[0]){
			return true;
		}else if(index==vals.length-1 && vals[index-1]<vals[index]){
			return true;
		}else if(index>0 && index<vals.length-1){
			return vals[index-1]<vals[index] && vals[index+1]<vals[index];
		}
		return false;
	}

}
