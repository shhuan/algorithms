package open.ex.zoj.easy.p3804;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {

	static int MAX_N = 50;
	static int N;
	static int M;
	static int F;
	static int K;
	static int[][][] STATUS = new int[2][MAX_N][MAX_N];
	static int CSI = 0;
	static int CT = 0; // current time
	static Map<Integer, List<Location>> LEAVE = new HashMap<>();
	static int T;

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		T = scanner.nextInt();
		for (int ti = 0; ti < T; ti++) {
			N = scanner.nextInt();
			M = scanner.nextInt();
			F = scanner.nextInt();
			K = scanner.nextInt();
			LEAVE.clear();
			CSI = 0;
			CT = 0;
			scanner.nextLine();
			for (int i = 0; i < N; i++) {
				char[] line = scanner.nextLine().toCharArray();
				for (int j = 0; j < M; j++) {
					STATUS[CSI][i][j] = line[j] - '0';
				}
			}
			for (int i = 0; i < K; i++) {
				int t = scanner.nextInt();
				int li = scanner.nextInt() - 1;
				int lj = scanner.nextInt() - 1;
				List<Location> ls = LEAVE.get(t);
				if (ls == null) {
					ls = new ArrayList<>();
					LEAVE.put(t, ls);
				}
				ls.add(new Location(li, lj));
			}
			for (int i = 0; i < F; i++) {
				update();
			}
			outputStatus();
		}
		scanner.close();

	}

	private static void outputStatus() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (STATUS[CSI][i][j] < 0) {
					System.out.print('X');
				} else {
					System.out.print(STATUS[CSI][i][j]);
				}
			}
			System.out.println();
		}
	}

	private static void update() {

		int nsi = CSI == 0 ? 1 : 0;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				STATUS[nsi][i][j] = STATUS[CSI][i][j];
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (STATUS[CSI][i][j] < 0) {
					continue;
				}
				int nb = neighbors(i, j);
				if (STATUS[CSI][i][j] == 1) {// awake
					if (nb < 2 || nb > 3) {
						STATUS[nsi][i][j] = 0;
					}
				} else {// asleep
					if (nb == 3) {
						STATUS[nsi][i][j] = 1;
					}
				}
			}
		}
		CT++;
		List<Location> ls = LEAVE.get(CT);
		if (ls != null) {
			for (Location loc : ls) {
				STATUS[nsi][loc.i][loc.j] = -1;
			}
		}
		CSI = nsi;
	}

	/**
	 * 
	 * not correct
	 * 
	 * @param li
	 * @param lj
	 * @return
	 */
	private static int neighbors(int li, int lj) {
		int c = 0;
		for (int i = -1; i <= 1; i++) {
			for (int j = -1; j <= 1; j++) {
				if (i == 0 && j == 0) {
					continue;
				}
				if (li + i > N - 1 || li + i < 0) {
					continue;
				}
				if (lj + j > M - 1 || lj + j < 0) {
					continue;
				}
				if (STATUS[CSI][li + i][lj + j] == 1) {
					c++;
				}
			}
		}
		return c;
	}

}

class Location {
	public int i;
	public int j;

	public Location(int i, int j) {
		super();
		this.i = i;
		this.j = j;
	}

}
