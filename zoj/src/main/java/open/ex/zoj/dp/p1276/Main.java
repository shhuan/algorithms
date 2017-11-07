package open.ex.zoj.dp.p1276;

import java.io.InputStream;
import java.util.Scanner;

/**
 * @author huash06
 * 
 * 
 * 				Optimal Array Multiplication Sequence
		Time Limit: 2 Seconds      Memory Limit: 65536 KB      Special Judge
		
		Given two arrays A and B, we can determine the array C = A B using the 
		standard definition of matrix multiplication:
		
		
		
		The number of columns in the A array must be the same as the number 
		of rows in the B array. Notationally, let's say that rows(A) and 
		columns(A) are the number of rows and columns, respectively, in the 
		A array. The number of individual multiplications required to compute 
		the entire C array (which will have the same number of rows as A and 
		the same number of columns as B) is then rows(A) columns(B) columns(A). 
		For example, if A is a 10 x 20 array, and B is a 20 x 15 array, it 
		will take 10 x 15 x 20, or 3000 multiplications to compute the C array.
		
		
		To perform multiplication of more than two arrays we have a choice 
		of how to proceed. For example, if X, Y, and Z are arrays, then to 
		compute X Y Z we could either compute (X Y) Z or X (Y Z). Suppose X is 
		a 5 x 10 array, Y is a 10 x 20 array, and Z is a 20 x 35 array. Let's 
		look at the number of multiplications required to compute the product 
		using the two different sequences:
		
		(X Y) Z
		
		
		5 x 20 x 10 = 1000 multiplications to determine the product (X Y), a 5 x 20 array.
		
		Then 5 x 35 x 20 = 3500 multiplications to determine the final result.
		
		Total multiplications: 4500.
		
		X (Y Z)
		
		10 x 35 x 20 = 7000 multiplications to determine the product (Y Z), a 10 x 35 array.
		
		Then 5 x 35 x 10 = 1750 multiplications to determine the final result.
		
		Total multiplications: 8750. 
		
		Clearly we'll be able to compute (X Y) Z using fewer individual multiplications.
		
		Given the size of each array in a sequence of arrays to be multiplied, 
		you are to determine an optimal computational sequence. Optimality, for this problem, 
		is relative to the number of individual multiplcations required.
		
		
		Input
		
		For each array in the multiple sequences of arrays to be multiplied you will be 
		given only the dimensions of the array. Each sequence will consist of an integer 
		N which indicates the number of arrays to be multiplied, and then N pairs of integers, 
		each pair giving the number of rows and columns in an array; the order in which the 
		dimensions are given is the same as the order in which the arrays are to be multiplied. 
		A value of zero for N indicates the end of the input. N will be no larger than 10.
		
		
		Output
		
		Assume the arrays are named A1, A2, ..., AN. Your output for each input case is 
		to be a line containing a parenthesized expression clearly indicating the order in 
		which the arrays are to be multiplied. Prefix the output for each case with the case 
		number (they are sequentially numbered, starting with 1). Your output should strongly 
		resemble that shown in the samples shown below. If, by chance, there are multiple correct 
		sequences, any of these will be accepted as a valid answer.
		
		
		Sample Input
		
		3
		1 5
		5 20
		20 1
		3
		5 10
		10 20
		20 35
		6
		30 35
		35 15
		15 5
		5 10
		10 20
		20 25
		0
		
		
		Sample Output
		
		Case 1: (A1 x (A2 x A3))
		Case 2: ((A1 x A2) x A3)
		Case 3: ((A1 x (A2 x A3)) x ((A4 x A5) x A6))
 * 
 *
 *
 *
 *
 *
 *
 *		===========EASY=================
 *		
 *		假设f(i,j)表示计算i到j之间的矩阵需要的最少计算次数，包括i和j， 1<=i,j<=N。
 *
 *		f(i,j) = min{f(i,k)+f(k,j)+g(i,k)*g(k,j)},i<=k<=j。
 *		g(i,j)表示i到j之间的矩阵做乘积之后的结果。
 *		f(i,i) = 0;
 *		
 *		计算时按照间隔从小到大的方式地推f即可。
 *
 *
 *
 *
 *
 *
 *
 */
public class Main {

	public static int MAX_N = 11;
	public static int G[][] = new int[MAX_N][MAX_N];
	public static int F[][] = new int[MAX_N][MAX_N];//i到j之间的矩阵做乘积需要的次数，包括i和j
	public static int M[][] = new int[MAX_N][2];//M[i][0]是矩阵i的行数，M[i][1]则是列数
	public static int N;
	
	public static InputStream input;
	public static boolean ONLINE_JUDGE = true;
	public static void main(String[] args) {
		if(ONLINE_JUDGE){
			input = System.in;
		}else{
			input = Main.class.getClassLoader().getResourceAsStream("input_1276.txt");
		}
		Scanner scanner = new Scanner(input);
		N = scanner.nextInt();
		int ci = 1;
		while(N!=0){
			for(int i=1;i<=N;i++){
				M[i][0] = scanner.nextInt();
				M[i][1] = scanner.nextInt();
			}
			System.out.print("Case "+ci+": ");
			ci++;
			cal();
			N = scanner.nextInt();
		}
		
		scanner.close();

	}
	
	public static void dp(){
		for(int i=1; i<=N; i++){
			for(int j=1; j<=N;j++){
				F[i][j] = 0;
			}
		}
		for(int gap=1;gap<N;gap++){
			for(int i=1; i<=N && i+gap<=N; i++){
				int j=i+gap;
				int mc = Integer.MAX_VALUE;
				int mk = i;
				for(int k=i;k<j;k++){
					int c = F[i][k]+F[k+1][j]+M[i][0]*M[k][1]*M[j][1];
					if(c<mc){
						mc = c;
						mk = k;
					}
				}
				F[i][j] = mc;
				G[i][j] = mk; 
			}
		}
	}
	public static void cal(){
		dp();
		System.out.print('(');
		outputResult(1,N);
		System.out.print(')');
		System.out.println();
	}
	public static void outputResult(int from, int to){
		if(from==to){
			System.out.print("A"+from);
		}else{
			int k = G[from][to];
			if(from<k){
				System.out.print('(');
			}
			outputResult(from,k);
			if(from<k){
				System.out.print(')');
			}
			System.out.print(" x ");
			if(k+1<to){
				System.out.print('(');
			}
			outputResult(k+1,to);
			if(k+1<to){
				System.out.print(')');
			}
		}
	}

}
