package open.ex.zoj.dp.p1303;

import java.io.InputStream;
import java.util.Scanner;


public class Main {

	public static int MAXN = 200;
	public static int MAXM = 20;
	public static int MAXD = MAXM*2*40;
	public static int F[][][] = new int[MAXN][MAXM][MAXD];
	public static int[][] J = new int[MAXN][2];// d=J[i][0];p=J[i][1]
	public static int N,M;

	public static InputStream input;
	public static boolean ONLINE_JUDGE = true;
	public static void main(String[] args) {
		if(ONLINE_JUDGE){
			input = System.in;
		}else{
			input = Main.class.getClassLoader().getResourceAsStream("input_1303.txt");
		}
		Scanner scanner = new Scanner(input);
		N = scanner.nextInt();
		M = scanner.nextInt();
		int ci = 1;
		while(N!=0 && M!=0){
			for(int i=1; i<=N; i++){
				J[i][0] = scanner.nextInt();
				J[i][1] = scanner.nextInt();
			}
			System.out.println("Jury #"+ci);
			ci++;
			cal();
			N = scanner.nextInt();
			M = scanner.nextInt();
		}
		scanner.close();

	}
	public static void cal(){
		dp();
		getResult();
	}

	public static void dp() {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= i; j++) {
				for (int k = 0; k <= M*2*40; k++) {
					F[i][j][k] = -1;
				}
			}
			int dmp = 0;
			int dap = 0;
			for(int j=1; j<=i; j++){
				dmp += J[j][0]-J[j][1];
				dap += J[j][0]+J[j][1];
			}
			dmp+=M*20;
			F[i][i][dmp]=dap;
		}

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j < i; j++) {
				int dmp = J[i][0]-J[i][1];//d minus p
				int dap = J[i][0]+J[i][1];//d add p
				for (int k = dmp+M*40; k <= M*2*40; k++) {
					int k1 = k - dmp;
					int p2 = F[i - 1][j][k];
					if(F[i - 1][j - 1][k1]>=0){
						int p1 = F[i - 1][j - 1][k1] + dap;
						F[i][j][k] = p1>p2?p1:p2;
					}else{
						F[i][j][k] = p2;
					}
				}
			}
		}
	}
	
	public static void getResult(){
		D=0;
		P=0;
		for(int k=0; k<=M*40; k++){
			int dap1 = F[N][M][k];
			int dap2 = F[N][M][2*M*40-k];
			if(dap1>0 || dap2>0){
				if(dap1>=dap2){
					deepSearch(N, M, k);
				}else{
					deepSearch(N, M, 2*M*40-k);
				}
				break;
			}
		}
		System.out.println();
	}
	
	public static int D;
	public static int P;
	
	public static void deepSearch(int i, int j, int k){
		if(i==1){
			System.out.println("Best jury has value "+D+" for prosecution and value "+P+" for defence:");
			return;
		}
		if(F[i-1][j][k]>0){
			deepSearch(i-1, j, k);
		}else{
			int dmp = J[i][0]-J[i][1];
			D += J[i][0];
			P += J[i][1];
			deepSearch(i-1, j-1, k-dmp);
			System.out.print(i+" ");
		}
	}

}
