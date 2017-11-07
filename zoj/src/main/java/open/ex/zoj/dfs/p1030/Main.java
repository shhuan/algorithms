package open.ex.zoj.dfs.p1030;

import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;

public class Main {

	public static int M; //number of cases.
	public static int N; //number of vertices
	public static int MAXN = 201;
	
	public static boolean G[][] = new boolean[MAXN][MAXN]; //关系图
	public static int[] X = new int[MAXN];
	public static int[] Y = new int[MAXN];
	public static int[] D = new int[MAXN];
	
	public static boolean ONLINE_JUDGE = false;

	public static void main(String[] args) {
		if(!ONLINE_JUDGE){
			System.setIn(Main.class.getClassLoader().getResourceAsStream("input_1030.txt"));
			try {
				System.setOut(new PrintStream(Main.class.getClassLoader().getResource("").getPath()+"output_1030.txt"));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}
		
		Scanner scanner = new Scanner(System.in);
		M = scanner.nextInt();
		while(M-->0){
			N = scanner.nextInt();
			for(int i=0; i<=N; i++){
				for(int j=0; j<=N; j++){
					G[i][j] = false;
				}
			}
			for(int i=0; i<N; i++){
				int vi = scanner.nextInt();
				int x = scanner.nextInt();
				int y = scanner.nextInt();
				int d = scanner.nextInt();
				for(int di=0; di<d; di++){
					int ti = scanner.nextInt();
					G[vi][ti] = true;
				}
				X[vi] = x;
				Y[vi] = y;
				D[vi] = d;
			}

			LEN = scanner.nextInt();
			cal();
		}
		scanner.close();
	}
	public static boolean[] VISITED = new boolean[210000]; 
	public static void cal(){
		COUNT = 0;
		for(int i=0; i<210000; i++){
			VISITED[i] = false;
		}
		for(int i=0; i<=N; i++){
			for(int j=i+1; j<=N; j++){
				if(G[i][j] && !VISITED[Integer.valueOf(String.valueOf(i)+String.valueOf(j))]){
					if(dfs(i,j,i,j,1,(Math.atan2(Y[i]-Y[j], X[i]-X[j])+2*Math.PI)%(2*Math.PI))){//i->j
					}
				}
			}
		}
		System.out.println(COUNT);
	}
	public static int COUNT = 0;
	public static int LEN = 0;
	public static boolean dfs(int ss, int st, int vs, int vt, int len, double theta){//从定点vs开始找到一条到vt长度为len的环
		if(len>LEN){
			return false;
		}
		
		double mint = Integer.MAX_VALUE;
		int nvt = 0; //next vt
		for(int i=1; i<=N; i++){
			if(i!=vs && G[vt][i]){
				double t = (Math.atan2(Y[i]-Y[vt],X[i]-X[vt]) +2*Math.PI)%(2*Math.PI);
				t = (2*Math.PI-t+theta)%(2*Math.PI);
				if(t<mint){
					mint = t;
					nvt = i;
				}
			}
		}
		if(nvt>0){
			if(len==LEN && vt==ss && nvt==st){
				//保证没有另外一个边延伸到多边形内部
				COUNT++;
				return true;
			}
			if(dfs(ss,st,vt,nvt,len+1, (Math.atan2(Y[vt]-Y[nvt], X[vt]-X[nvt])+2*Math.PI)%(2*Math.PI))){
				VISITED[Integer.valueOf(String.valueOf(vt)+String.valueOf(nvt))] = true;
				return true;
			}
		}
		return false;
	}

}
