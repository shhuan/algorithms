package op.ex.common.unclsfd;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Scanner;

public class Google_MineSweeper {

	public static final int MAXN = 300;
	public static char[][] Board = new char[MAXN][MAXN];
	public static int[][] Count = new int[MAXN][MAXN];
	public static int N = 0;

	public static boolean ONLINE_JUDGE = false;

	public static void main(String[] args) {
		if (!ONLINE_JUDGE) {
			System.setIn(Google_MineSweeper.class.getClassLoader().getResourceAsStream("A-small-practice.in"));
			// System.setIn(Google_MineSweeper.class.getClassLoader().getResourceAsStream("input_mine_sweeper.txt"));

			try {
				System.setOut(new PrintStream(new FileOutputStream("D:\\tmp\\A-small-practice.out")));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}

		Scanner scanner = new Scanner(System.in);
		int T = scanner.nextInt();
		for (int ti = 1; ti <= T; ti++) {
			N = scanner.nextInt();
			scanner.nextLine();
			for (int row = 0; row < N; row++) {
				String line = scanner.nextLine();
				for (int col = 0; col < N; col++) {
					char ch = line.charAt(col);
					Board[row][col] = ch;
					if (ch == '*') {
						Count[row][col] = -1;
					} else {
						Count[row][col] = 0;
					}
				}
			}
			System.out.println("Case #" + ti + ": " + sweep());
		}
		scanner.close();
	}

	private static int sweep() {
		int[][] deltas = new int[][] { { -1, 0 }, { 1, 0 }, { -1, -1 }, { -1, 1 }, { 0, -1 }, { 0, 1 }, { 1, -1 },
				{ 1, 1 } };

		// 计算每个格子的数字, -1表示已经扫除或者是雷
		for (int ri = 0; ri < N; ri++) {
			for (int ci = 0; ci < N; ci++) {
				if (Board[ri][ci] == '*') {
					for (int di = 0; di < 8; di++) {
						int r = ri + deltas[di][0];
						int c = ci + deltas[di][1];
						if (r >= 0 && r < N && c >= 0 && c < N && Count[r][c] >= 0) {
							Count[r][c] += 1;
						}
					}
				}
			}
		}

		int step = 0;

		// 扫除所有的0
		for (int ri = 0; ri < N; ri++) {
			for (int ci = 0; ci < N; ci++) {
				step += expand(ri, ci);
			}
		}

		// 扫除所有其他数字
		for (int ri = 0; ri < N; ri++) {
			for (int ci = 0; ci < N; ci++) {
				if (Count[ri][ci] > 0) {
					step++;
				}
			}
		}
		return step;
	}

	private static int expand(int ri, int ci) {
		if (Count[ri][ci] == 0) {
			Count[ri][ci] = -1;
			int[][] deltas = new int[][] { { -1, 0 }, { 1, 0 }, { -1, -1 }, { -1, 1 }, { 0, -1 }, { 0, 1 }, { 1, -1 },
					{ 1, 1 } };
			for (int di = 0; di < 8; di++) {
				int r = ri + deltas[di][0];
				int c = ci + deltas[di][1];
				if (r >= 0 && r < N && c >= 0 && c < N) {
					if (Count[r][c] == 0) {
						expand(r, c);
					} else {
						Count[r][c] = -1;
					}

				}
			}
			return 1;
		}
		return 0;
	}

}
