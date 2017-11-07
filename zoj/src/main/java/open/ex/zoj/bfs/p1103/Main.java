package open.ex.zoj.bfs.p1103;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

/**
 * @author huash06
 *
 *
 *         题意： 游戏中有3个棋子，给定初始时候3个棋子的位置，问经过最少多少步所有的棋子可以走到同一点。
 *         棋子只能沿着这样一条路线移动，它的颜色和另外两个棋子之间的连线的颜色一样
 * 
 *         分析： 广度搜索即可，需要保存搜索过的位置
 */
public class Main {
	public static int MAXN = 51;
	public static char[][] M = new char[MAXN][MAXN];
	public static int N;
	public static boolean ONLINE_JUDGE = true;
	public static boolean[][][] TRAVELED = new boolean[MAXN][MAXN][MAXN];// 这种状态是否搜索过

	public static void main(String[] args) {
		if (!ONLINE_JUDGE) {
			System.setIn(Main.class.getClassLoader().getResourceAsStream("input_1103.txt"));
		}

		Scanner scanner = new Scanner(System.in);

		while ((N = scanner.nextInt()) != 0) {
			for (int i = 0; i < MAXN; i++) {
				for (int j = 0; j < MAXN; j++) {
					for (int k = 0; k < MAXN; k++) {
						TRAVELED[i][j][k] = false;
					}
				}
			}
			int s1 = scanner.nextInt();
			int s2 = scanner.nextInt();
			int s3 = scanner.nextInt();
			State state = new State(s1, s2, s3, 0);

			scanner.nextLine();
			for (int i = 1; i <= N; i++) {
				String[] line = scanner.nextLine().split("\\s+");
				for (int j = 1; j <= N; j++) {
					M[i][j] = line[j - 1].charAt(0);
				}
			}

			Queue<State> q = new PriorityQueue<State>(MAXN * MAXN * MAXN, new Comparator<State>() {
				@Override
				public int compare(State s1, State s2) {
					return s1.steps - s2.steps;
				}
			});
			addNewState(q, state);
			boolean found = false;
			while (!q.isEmpty()) {
				state = q.poll();
				if (state.isAtSamePlace()) {
					System.out.println(state.steps);
					found = true;
					break;
				}

				// 移动棋子1
				for (int i = 1; i <= N; i++) {
					if (M[state.pos1][i] == M[state.pos2][state.pos3]) {
						State nextState = new State(i, state.pos2, state.pos3, state.steps + 1);
						addNewState(q, nextState);
					}
				}

				// 移动棋子2
				for (int i = 1; i <= N; i++) {
					if (M[state.pos2][i] == M[state.pos1][state.pos3]) {
						State nextState = new State(state.pos1, i, state.pos3, state.steps + 1);
						addNewState(q, nextState);
					}
				}

				// 移动棋子3
				for (int i = 1; i <= N; i++) {
					if (M[state.pos3][i] == M[state.pos1][state.pos2]) {
						State nextState = new State(state.pos1, state.pos2, i, state.steps + 1);
						addNewState(q, nextState);
					}
				}

			}
			if (!found) {
				System.out.println("impossible");
			}
		}

		scanner.close();
	}

	private static void addNewState(Queue<State> q, State state) {
		if (!TRAVELED[state.pos1][state.pos2][state.pos3]) {
			// System.out.println(state);
			TRAVELED[state.pos1][state.pos2][state.pos3] = true;
			q.add(state);
		}
	}

}

class State {
	int pos1;
	int pos2;
	int pos3;
	int steps;

	public State(int pos1, int pos2, int pos3, int steps) {
		super();
		this.pos1 = pos1;
		this.pos2 = pos2;
		this.pos3 = pos3;
		this.steps = steps;
	}

	public boolean isAtSamePlace() {
		return pos1 == pos2 && pos2 == pos3;
	}

	@Override
	public String toString() {
		return "State [pos1=" + pos1 + ", pos2=" + pos2 + ", pos3=" + pos3 + ", steps=" + steps + "]";
	}
}
