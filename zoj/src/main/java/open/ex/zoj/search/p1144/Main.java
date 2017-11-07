package open.ex.zoj.search.p1144;

import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;

/**
 * @author huash
 *
 *         题意：有个抢劫犯在城市中移动，程序给出一些时间点和相应的区域，表示在某个时间点在某个区域内没有罪犯。
 *         问能否根据这些信息确定每个时间点罪犯所在的位置。
 * 
 *         分析：根据每个时间点t的信息可以推断出时间t＋1时候罪犯可能在的位置，如果在最终时间T罪犯依然可能有位置藏身那么罪犯就在城市中。
 *         在根据最后时刻罪犯所在的位置反推前一个时间罪犯可能的位置，最终得到的每个时间点罪犯可能在的位置。
 */
public class Main {
	public static boolean ONLINE_JUDGE = true;
	public static int MAXN = 102;
	public static boolean M[][][] = new boolean[MAXN][MAXN][MAXN];// M[t][x][y]==true表示时间t时,罪犯可能在位置x,y
	public static int[] X = new int[MAXN];// X[t]表示时间t时候罪犯所在位置的x坐标
	public static int[] Y = new int[MAXN];// Y[t]表示时间t时候罪犯所在位置的y坐标
	public static int[] COUNT = new int[MAXN];// COUNT[t]表示时间t时候罪犯可能的位置个数

	public static void main(String[] args) {
		if (!ONLINE_JUDGE) {
			System.setIn(Main.class.getClassLoader().getResourceAsStream("input_1144.txt"));
//			try {
//				System.setOut(new PrintStream(Main.class.getClassLoader().getResource("").getPath() + "output_1144.txt"));
//			} catch (FileNotFoundException e) {
//				e.printStackTrace();
//			}
		}

		Scanner scanner = new Scanner(System.in);
		int caseIndex = 1;
		int W, H, T;
		while (scanner.hasNextInt()) {
			W = scanner.nextInt();
			H = scanner.nextInt();
			T = scanner.nextInt();
			if (W == 0 && H==0 && T==0) {
				break;
			}
			System.out.println(String.format("Robbery #%d:", caseIndex++));

			for (int i = 1; i <= T; i++) {
				for (int j = 1; j <= W; j++) {
					for (int k = 1; k <= H; k++) {
						M[i][j][k] = true;
					}
				}
				COUNT[i] = 0;
				X[i]  = 0;
				Y[i] = 0;
			}
			int count = scanner.nextInt();
			for (int i = 0; i < count; i++) {
				int ti, l, r, b, t;
				ti = scanner.nextInt();
				l = scanner.nextInt();
				b = scanner.nextInt();
				r = scanner.nextInt();
				t = scanner.nextInt();
				for (int x = l; x <= r; x++) {
					for (int y = b; y <= t; y++) {
						M[ti][x][y] = false;
					}
				}
			}
			// 向前推
			for (int t = 2; t <= T; t++) {
				for (int x = 1; x <= W; x++) {
					for (int y = 1; y <= H; y++) {
						if (M[t][x][y]) {
							M[t][x][y] = M[t - 1][Math.max(x - 1, 1)][y] || M[t - 1][Math.min(x + 1, W)][y]
									|| M[t - 1][x][Math.max(y - 1, 1)] || M[t - 1][x][Math.min(y + 1, H)];
						}
					}
				}
			}
			boolean exist = false;
			for (int x = 1; x <= W && !exist; x++) {
				for (int y = 1; y <= H && !exist; y++) {
					if (M[T][x][y]) {
						exist = true;
					}
				}
			}
			if (!exist) {
				System.out.println("The robber has escaped.");
				System.out.println();
				continue;
			}
			// 反向推导
			for (int t = T - 1; t >= 1; t--) {
				for (int x = 1; x <= W; x++) {
					for (int y = 1; y <= H; y++) {
						if (M[t][x][y]) {
							M[t][x][y] = M[t + 1][Math.max(x - 1, 1)][y] || M[t + 1][Math.min(x + 1, W)][y]
									|| M[t + 1][x][Math.max(y - 1, 1)] || M[t + 1][x][Math.min(y + 1, H)];
						}
					}
				}
			}

			// 计算每个时间点有多少个位置可以藏身
			for (int t = 1; t <= T; t++) {
				for (int x = 1; x <= W; x++) {
					for (int y = 1; y <= H; y++) {
						if (M[t][x][y]) {
							COUNT[t]++;
							X[t] = x;
							Y[t] = y;
						}
					}
				}
			}

			boolean nothingKnown = true;
			for (int t = 1; t <= T; t++) {
				if (COUNT[t] == 1) {
					System.out.println(String.format("Time step %d: The robber has been at %d,%d.", t, X[t], Y[t]));
					nothingKnown = false;
				}
			}
			if (nothingKnown) {
				System.out.println("Nothing known.");
			}
			System.out.println();

		}

		scanner.close();

	}

}
