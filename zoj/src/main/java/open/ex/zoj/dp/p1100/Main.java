package open.ex.zoj.dp.p1100;

import java.util.Scanner;

/**
 * @author huash06
 *
 *
 *
 * 题意：往一个矩形（H*W）填满横着或者竖着放的2*1的小矩形，计算总共有多少种放法
 * 
 * 
 * 分析：从上往下放，由于每一行i+1的状态依赖于上面一行i（i>0)的状态，我们可以先找出每一种行状态对应的下一行的状态（DFS）。
 * 假设每个单元格的状态用0和1分别表示填满和没填满，可以用一个整数表示一行的状态。
 * 
 * 假设第一行上面还有一行边界，即第0行的状态全是1.
 * 第0行全是1的状态可以摆出n1种下面一行（第1行）的状态。
 * 这n1种状态又分别可以摆出n2i种第2行的状态得到。
 * 。。。
 * 一直递推到最下面一行
 * c[0][(1<<w)-1]=1;//第一行状态全是1的数量是1
 * c[i+1][to] = Σc[i][fromi];//有多种状态from1,from2,...,fromi可能使得下一行的状态为to
 * 最终结果是第H行全是1的数量，即c[h][(1<<W)-1]。
 * 
 * 
 * 状态转换：
 * 对于某一行行的第j列，有三种摆放方式：横着放，竖着放，不放。
	dfs(j+2,(from<<2)+3,(to<<2)+3); //横着放，这层和下一层匹配的都是两位1，3就是二进制11
	dfs(j+1,(from<<1)+1,to<<1);//竖着放，这层多一个1,匹配下层这个位置是0
	dfs(j+1,from<<1,(to<<1)+1);//不放，这层多一个0，匹配的下层多个1
 * 
 * 
 * 
 * 
 * 
 * 
 */
public class Main {

	public static int H;
	public static int W;
	public static int[] FROM = new int [14000];//状态FROM[i]可以使得上面一行的状态为TO[i]
	public static int[] TO = new int [14000];//状态数量F[i]=F[i-2]+2*F[i-1],F[1]=2,F[2]=4,F[11]=11482
	public static Long[][] C = new Long[12][2100];//最多11行，每行2^11=2048个状态
	
	public static boolean ONLINE_JUDGE = true;
	public static void main(String[] args) {
		if(!ONLINE_JUDGE){		
	        System.setIn(Main.class.getClassLoader().getResourceAsStream("input_1100.txt"));
	    }  
		Scanner scanner = new Scanner(System.in);
		H = scanner.nextInt();
		W = scanner.nextInt();
		while(!(H==0 && W==0)){
			init();
			dfs(0, 0, 0);
			dp();
			H = scanner.nextInt();
			W = scanner.nextInt();
		}
		scanner.close();

	}
	
	public static void init(){
		for(int i=0; i<12; i++){
			for(int j=0; j<2100; j++){
				C[i][j] = 0L;
			}
		}
		SI=0;
		for(int i=0; i<14000; i++){
			FROM[i] = 0;
			TO[i] = 0;
		}
	}
	
	public static int SI = 0;
	public static void dfs(int col, int from, int to){
		if(col>W){
			return;
		}
		if(col==W){
			FROM[SI] = from;
			TO[SI] = to;
			SI++;
			return;
		}
		dfs(col+2, (from<<2)+3, (to<<2)+3);
		dfs(col+1, (from<<1)+1, to<<1);
		dfs(col+1, from<<1, (to<<1)+1);
	}
	public static void dp(){
		C[0][(1<<W)-1]=1L;
		//c[i+1][to] = Σc[i][fromi];//有多种状态from1,from2,...,fromi可能使得下一行的状态为to
		for(int i=0; i<H; i++){
			for(int si=0; si<SI; si++){
				C[i+1][TO[si]] += C[i][FROM[si]];
			}
		}
		System.out.println(C[H][(1<<W)-1]);
	}

}

