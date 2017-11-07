package open.ex.zoj.dp.p3160;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.util.Random;

public class CaseGenerator {

	public static void main(String[] args) {
		PrintStream ps;		
		try {
			ps = new PrintStream(new FileOutputStream("input_3160.txt"));
	        System.setOut(ps); 
			int T = 10000;
			
			for(int i=0; i<T; i++){
				generateCase();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

	private static void generateCase() {
		Random rand = new Random();
		int N = rand.nextInt(10)+2;
		int M = rand.nextInt(N*N/2);
		System.out.println(N+" "+M);
		for(int i=0; i<M; i++){
			System.out.println(rand.nextInt(N)+" "+rand.nextInt(N));
		}
		int[] A = new int[N];
		for(int i=0; i<N; i++){
			A[i] = i;
		}
		int p = rand.nextInt(100);
		for(int i=0; i<p; i++){
			nextPermutation(A);
		}
		for(int i=0; i<N; i++){
			System.out.print(A[i]+" ");
		}
		System.out.println();
		System.out.println();
		
		
	}
	
	public static boolean nextPermutation(int[] arr){
		if(arr==null || arr.length<=1){
			return false;
		}
		for(int ii=arr.length-1; ii>0; ii--){
			int i = ii-1;
			if(arr[i]<arr[ii]){
				int j=arr.length-1;
				for(; j>=0; j--){
					if(arr[i]<arr[j]){
						break;
					}
				}
				if(j>0){
					swap(arr, i, j);
					reverse(arr, ii, arr.length-1);
					return true;
				}
			}
		}
		reverse(arr, 0, arr.length-1);
		return false;
	}
	public static void swap(int[] arr, int swi, int swj){
		int tmp = arr[swi];
		arr[swi] = arr[swj];
		arr[swj] = tmp;
	}
	public static void reverse(int[] arr, int ri, int rj){
		while(ri<rj){
			swap(arr, ri, rj);
			ri++;
			rj--;
		}
	}

}
