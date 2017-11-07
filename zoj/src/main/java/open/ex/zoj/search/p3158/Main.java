package open.ex.zoj.search.p3158;

import java.io.InputStream;
import java.util.Scanner;

/**
 * @author huash06
 *
 *
 *
	李雷和韩梅梅搞暧昧情人节分蛋糕吃，蛋糕由m*n单元小块组成，每小
	块包含一定的营养价值。现在要求将蛋糕延纵向分成锯齿形的两块，
	要求两块的营养价值之差尽量地小。如果答案大于某给定值t，则输出
	“You’d better buy another one!”。
	

		对于每一行，都要从某一位置分成两段，由于不能切出0长度的一段，
		所以有n − 1个选择，一共m行，就是(n − 1)m种方案。由于问题的规模很
		小，暴力枚举所有情况取最优解就可以了。通过预处理和递归可以实现时
		间复杂度为n^m的程序。

 */
public class Main {
	
	public static int MAXN = 7;

	public static int N;
	public static int M;
	public static int[][] V = new int[MAXN][MAXN];
	public static int D;
	public static int T;
	public static InputStream input;
	public static boolean ONLINE_JUDGE = true;
	public static void main(String[] args) {
		if(ONLINE_JUDGE){
			input = System.in;
		}else{
			input = Main.class.getClassLoader().getResourceAsStream("input_3158.txt");
		}
		Scanner scanner = new Scanner(input);
		while(scanner.hasNextInt()){
			M = scanner.nextInt();
			N = scanner.nextInt();
			
			for(int i=0; i<M; i++){
				for(int j=0; j<N; j++){
					V[i][j] = scanner.nextInt();
				}
			}
			T = scanner.nextInt();
			D = Integer.MAX_VALUE;
			search(0, 0);
			if(D>T){
				System.out.println("You'd better buy another one!");
			}else{
				System.out.println(D);
			}
		}
		
		scanner.close();
		
	}
	
	public static void search(int row, int diff){
		if(row>= M){
			diff = Math.abs(diff);
			D = D>diff?diff:D;
			return;
		}
		int tv = 0;
		for(int i=0; i<N; i++){
			tv += V[row][i];
		}
		int cv = V[row][0];
		for(int i=1 ; i<N; i++){
			search(row+1, diff+(2*cv-tv));
			cv += V[row][i];
		}
	}

}
