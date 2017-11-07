package open.ex.zoj.dp.p1499;

import java.io.InputStream;
import java.util.Scanner;


/**
 * @author huash06
 * 
 * 
 * 					Increasing Sequences
		Time Limit: 10 Seconds      Memory Limit: 32768 KB
		
		Given a string of digits, insert commas to create a sequence of 
		strictly increasing numbers so as to minimize the magnitude of 
		the last number. For this problem, leading zeros are allowed in front of a number.
		
		
		Input
		
		Input will consist of multiple test cases. Each case will 
		consist of one line, containing a string of digits of maximum
		 length 80. A line consisting of a single 0 terminates input.
		
		
		Output
		
		For each instance, output the comma separated strictly 
		increasing sequence, with no spaces between commas or numbers. 
		If there are several such sequences, pick the one which has the 
		largest first value; if there's a tie, the largest second number, etc.



 * 
 * 	1. 字符串比较长不能把字符串表示成数字，写一个方法来比较大小
	2. 设f(i,j)=max{t,f(i-j,t)>0&&atoi(i-j,i)>atoi(i-j-t,i-j)},
		表示第i个数之前j位构成一个数的符合严格递增的序列，
		这个序列是从前i-j个数构成的序列递推来的，而这个t是第i-j个数
		前t（量大的）位构成的数比第i个数前j位构成的数小，所以说相应的
		t-1,t-2,…1位都比这个数小。
		
			t      j   i
		|_______|______|
		
		求出来f(i,j)之后,正向推导符合要求的分割。
		
			t      j   i
		|_______|______|
		gi  gt    j    i
		
		设g(gi,gt)=max{j},表示到gi位置(gi前面的已经划分完毕，不包括gi)找到满足条件的序列后，
		 接来下应该有j个数字，j取最大值，j满足条件f(i,j)>=t。
		并且通过j能够推导到最后使得最后一个数字最小，即从前往后取最长的子串，并且最后个子串的值最小。
		gi+gt+j-1=i<=N-1
				=>j<=N-gi-t
		
 * 
 * 
 *
 */
public class Main {

	public static int MAX_N = 81;
	public static int[][] F = new int[MAX_N][MAX_N + 1];
	public static char[] S = new char[MAX_N];
	public static int N;

	public static InputStream input;
	public static boolean ONLINE_JUDGE = true;
	public static void main(String[] args) {
		if(ONLINE_JUDGE){
			input = System.in;
		}else{
			input = Main.class.getClassLoader().getResourceAsStream("input_1499.txt");
		}
		Scanner scanner = new Scanner(input);
		String input = scanner.nextLine();
		while (!input.equalsIgnoreCase("0")) {
			S = input.toCharArray();
			N = input.length();
			cal();
			input = scanner.nextLine();
		}
		scanner.close();
	}

	public static void cal(){
		f();
		cg();
	}

	/**
	 * Calculate value of F[i][j]
	 */
	public static void f() {
		for (int i = 0; i < N; i++) {
			for (int j = 1; j <= i + 1; j++) {
				F[i][j] = -1;
			}
			F[i][i+1]=0;
		}

		for (int i = 0; i < N; i++) {
			for (int j = 1; j <= i + 1; j++) {
				int i1 = i-j;
				for (int t = i - j + 1; t > 0; t--) {
					
					if (F[i1][t] >= 0 && compareFij(i, j, i1, t) > 0) {
						F[i][j] = t;
						break;
					}
				}
			}
		}

	}
	
	/**
	 * Search route to final minimum last value from g.
	 */
	public static void cg(){
		boolean found = false;
		for(int t=N-1; t>=0; t--){
			if(g(0,t,0)){
				found = true;
				break;
			}
		}
		if(!found){
			INDICES[0]=N;
		}
		int ii=0;
		for(int i=0; i<N; ii++){
			while(i<N && i<INDICES[ii]){
				System.out.print(S[i]);
				i++;
			}
			if(i<N){
				System.out.print(',');
			}
		}
		System.out.println();
	}
	/**
	 * 
	 * 
	 *  g(gi,gt)=max{j},表示到gi位置(gi前面的已经划分完毕，不包括gi)找到满足条件的序列后，
		 接来下应该有j个数字，j取最大值。
		 j满足条件f(i,j)>=t
				t     j   i 
			|______|______|
			gi  gt    j   i

			t=gt, 
			
			gi+gt+j-1=i<=N-1
				=>j<=N-gi-t
	 * 
	 * 
	 * INDICES中保存分割的位置，INDICES[i]=j表示第i个分隔符位于第j个数字字符之后。
	 * 
	 * @param gi start index
	 * @param gt length of segment
	 * @param ii index of INDICES
	 * @return true if it reach final minimum last value.
	 */
	public static int[] INDICES = new int[MAX_N];
	public static boolean g(int gi, int gt, int ii){		
		if(gi+gt>N){
			return false;
		}
		
		//gi开始,长度为gt的数字如果全部是0，则这段序列不能单独成为一个数字
		boolean isZero = true;
		for(int i=gi;i<gi+gt;i++){
			if(S[i]>'0'){
				isZero = false;
				break;
			}
		}
		if(isZero){
			return false;
		}
		
		for(int j=N-gi-gt;j>0;j--){
			int i = gi+gt+j-1;
			if(F[i][j]>=gt){
				if(i==N-1){//如果到了最后的位置，选取的j需要满足最后个数字最小
					boolean found = true;
					for(int k=1; k<j;k++){
						if(F[i][k]>0 && compareFij(i,k,i,j)<0){
							found = false;
							break;
						}
					}
					if(found){
						INDICES[ii] = gi+gt;
						INDICES[ii+1] = N;
						return true;
					}
				}
				INDICES[ii] = gi+gt;
				if(g(gi+gt,j,ii+1)){
					return true;
				}
			}
		}
		return false;
	}
		
	public static int compareFij(int i1, int j1, int i2, int j2) {// 比较f(i1,j1)和f(i2,j2)
		return compare(i1 - j1 + 1, i1, i2 - j2 + 1, i2);
	}

	public static int compare(int i1, int j1, int i2, int j2) {// 比较[i1,j1]组成的数字和[i2,j2]组成的数字的值
		int l1 = j1 - i1 + 1;
		int l2 = j2 - i2 + 1;

		if (l1 < l2) {
			return -compare(i2, j2, i1, j1);
		}

		if (l1 > l2) {
			for (int i = i1; i < i1 + l1 - l2; i++) {
				if (S[i] > '0') {
					return 1;
				}
			}
			return compare(i1 + l1 - l2, j1, i2, j2);
		}
		for (int i = 0; i < l1; i++) {
			if (S[i1 + i] > S[i2 + i]) {
				return 1;
			} else if (S[i1 + i] < S[i2 + i]) {
				return -1;
			}
		}
		return 0;
	}
}
