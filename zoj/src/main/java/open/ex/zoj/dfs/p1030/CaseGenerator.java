package open.ex.zoj.dfs.p1030;

import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Random;

public class CaseGenerator {

	public static void main(String[] args) {
		try {
			System.setOut(new PrintStream(CaseGenerator.class.getClassLoader().getResource("input_1030.txt").getPath()));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		int caseCount = 100;
		System.out.println(caseCount);
		for(int i=0; i<caseCount; i++){
			generateCase();
		}
	}
	
	public static void generateCase(){
		Random rand = new Random();
		int N = rand.nextInt(10)+1;
		System.out.println(N);
		boolean G[][] = new boolean[N+1][N+1];
		int[][] XY = new int[N+1][2];
		for(int i=1; i<=N; i++){
			XY[i][0] = rand.nextInt(20);
			XY[i][1] = rand.nextInt(20);
		}
		int links = rand.nextInt(N*3)+N;
		for(int i=0; i<links; i++){
			int s = rand.nextInt(N)+1;
			int ss = s;
			for(int j=0; j<rand.nextInt(3);j++){
				int t = rand.nextInt(N)+1;
				if(s!=t){
					G[s][t] = true;
					G[t][s] = true;
					s = t;
				}
			}
			if(s!=ss){
				G[s][ss] = true;
				G[ss][s] = true;
			}
		}
		for(int i=1; i<=N; i++){
			StringBuilder line = new StringBuilder();
			line.append(i+" ");
			line.append(XY[i][0]+" "+XY[i][1]+" ");
			int d = 0;
			for(int j=1; j<=N; j++){
				if(j!=i && G[i][j]){
					d++;
				}
			}
			line.append(d);
			for(int j=1; j<=N; j++){
				if(j!=i && G[i][j]){
					line.append(" "+j);
				}
			}
			System.out.println(line.toString());
		}
		System.out.println(rand.nextInt(N/2+1)+2);
	}

}
