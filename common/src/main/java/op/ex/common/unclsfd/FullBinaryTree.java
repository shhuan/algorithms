package op.ex.common.unclsfd;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Date;
import java.util.Scanner;

public class FullBinaryTree {

	static int MAXN = 1001;
	static int N = 10;
	static boolean[][] G = new boolean[MAXN][MAXN];
	public static boolean ONLINE_JUDGE = false;

	public static void main(String[] args) {
		if (!ONLINE_JUDGE) {
			System.setIn(Google_MineSweeper.class.getClassLoader().getResourceAsStream("FullBinaryTree-Large.in"));
//			System.setIn(Google_MineSweeper.class.getClassLoader().getResourceAsStream("sample.txt"));

//			try {
//				System.setOut(new PrintStream(new FileOutputStream("D:\\tmp\\FullBinaryTree.out")));
//			} catch (FileNotFoundException e) {
//				e.printStackTrace();
//			}
		}
		long startTime = new Date().getTime();
		Scanner scanner = new Scanner(System.in);
		int T = scanner.nextInt();
		for (int ti = 1; ti <= T; ti++) {
			N = scanner.nextInt();
			for(int i=0; i<=N; i++){
				for(int j=0; j<=N; j++){
					G[i][j] = false;
				}
			}
			for(int i=0; i<N-1; i++){
				int s = scanner.nextInt();
				int t = scanner.nextInt();
				G[s][t] = true;
				G[t][s] = true;
			}
			
			int count = N;
			for(int i=1; i<=N; i++){
				int[] cr = bt(i, -1);
				if(cr[0] < count){
					count = cr[0];
				}
			}
			System.out.println(String.format("Case #%d: %d", ti, count));
		}
		long endTime = new Date().getTime();
		System.err.println("Time Cost: "+(endTime-startTime)/1000.0+"s");

		scanner.close();
	}
	
	
	static int[] bt(int root, int parent){
		int[] CHILDREN = new int[N];
		int childrenCount = 0;
		for(int i=1; i<=N; i++){
			if(i!=parent && G[root][i]){
				CHILDREN[childrenCount++] = i; 
			}
		}
		if(childrenCount == 0){
			return new int[]{0, 1};
		}else if(childrenCount == 1){
			int[] cbt = bt(CHILDREN[0], root);
			return new int[]{cbt[0]+cbt[1], 1};
		}else if(childrenCount == 2){
			int[] cbt1 = bt(CHILDREN[0], root);
			int[] cbt2 = bt(CHILDREN[1], root);
			return new int[]{cbt1[0]+cbt2[0], cbt1[1]+cbt2[1]+1};
		}else{
			int[][] CHILDREN_CBT = new int[childrenCount][2];
			for(int i=0; i<childrenCount; i++){
				CHILDREN_CBT[i] = bt(CHILDREN[i], root);
			}
			Arrays.sort(CHILDREN_CBT, new Comparator<int[]>(){

				@Override
				public int compare(int[] v1, int[] v2) {
					return v1[1] - v2[1];
				}
			});
			
			int cutted = 0;			
			for(int i=0; i<childrenCount; i++){
				cutted += CHILDREN_CBT[i][0] + CHILDREN_CBT[i][1];
			}
			cutted -= CHILDREN_CBT[childrenCount-1][1];
			cutted -= CHILDREN_CBT[childrenCount-2][1];
			return new int[]{cutted, CHILDREN_CBT[childrenCount-1][1]+CHILDREN_CBT[childrenCount-2][1]+1};
		}		
	}

}
