package open.ex.zoj.dp.p3160;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;

/**
 * @author huash06
 * 
 * 

		不超过300个人坐成一排，如果相邻两人有八卦关系，那么这两个人可
		以私奔，问最优方案下可以有多少人私奔。
		这是一个很经典 的动态规划问题。注意初始状态是0 n − 1的一个排
		列，需要处理一下。
		记f[l][r]表示从l到r这一段的人是否可以集体私奔。那么f[l][r]为真有两
		种情况：
		• 位置l和r的人有八卦关系且f[l + 1][r − 1]为真；
		• 存在某个m使得f[l][m]和f[m + 1][r]均为真。
		于是可以动态规划求出所有的f[i][j]，复杂度为O(n^3)。
		然后记g[n]为前n人最少留下的人数，那么有
		
		g[0] = 0
		g[i] = min {g[i − 1] + 1, min j<i,f[j][i]=True g[j]}
		这一段复杂度为O(n^2)，答案就是n − dp[n]。

 *
 */
public class Main {

	public static int N;
	public static int M;
	public static int MAXN = 301;
	public static boolean [][] R = new boolean[MAXN][MAXN];
	public static boolean [][] F = new boolean[MAXN][MAXN];
	public static int[] G = new int[MAXN];
	public static int[] A = new int[MAXN];
	
	
	public static boolean ONLINE_JUDGE = true;
	public static void main(String[] args) {
		if(!ONLINE_JUDGE){		
//	        System.setIn(Main.class.getClassLoader().getResourceAsStream("input_3160.txt"));
			try {
				System.setIn(new FileInputStream("C:\\Users\\huash06\\git\\Algorithms\\zoj\\input_3160.txt"));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
			try {
				System.setOut(new PrintStream("C:\\Users\\huash06\\git\\Algorithms\\zoj\\output_3160.txt"));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
	    }  
	
		Scanner scanner = new Scanner(System.in);
		while(scanner.hasNextInt()){
			N = scanner.nextInt();
			M = scanner.nextInt();
			for(int i=0; i<MAXN; i++){
				for(int j=0; j<MAXN; j++){
					R[i][j] = false;
					F[i][j] = false;
				}
			}
			for(int i=0; i<M; i++){
				int a = scanner.nextInt();
				int b = scanner.nextInt();
				R[a][b] = true;
				R[b][a] = true;
			}
			for(int i=0; i<N; i++){
				A[i] = scanner.nextInt();
			}
			cal();
		}
		scanner.close();

	}
	
	public static void cal(){
		dp();
//		outputF();
		cg();
		
		
	}
	public static void outputF(){
		for(int i=0; i<N; i++){
			for(int j=0; j<N; j++){
				System.out.print((F[i][j]?"T":"0")+" ");
			}
			System.out.println();
		}
		System.out.println();
	}
	public static void cg(){
		G[0] = 0;
		for(int i=1; i<=N; i++){//i个人
			int g = G[i-1]+1;
			for(int j=0; j<i-1; j++){
				if(F[j][i-1]){//i个人，序号i-1
					g = g>G[j]?G[j]:g;
				}
			}
			G[i] = g;
		}
		System.out.println(N-G[N]);
	}
	public static void dp(){
		for(int gap = 1; gap<N ;gap++){
			for(int l=0; l<N-1; l++){
				int r = l+gap;
				if(r>N-1){
					break;
				}
				//[l,r]的人全部私奔的两种情况
				//情况1，A[l]和A[r]私奔
				if(R[A[l]][A[r]]){//注意即使A[l]和A[r]能够私奔，也不表示这是最佳情况。这里卡了很久
					if(l==r-1 || F[l+1][r-1]){
						F[l][r] = true;
						continue;
					}
				}
				//情况2，[l,m]和[m+1,r]的人全部私奔
				for(int m=l+1;m<r-1;m++){
					if(F[l][m] && F[m+1][r]){
						F[l][r] = true;
						break;
					}
				}
			}
		}
	}

}
