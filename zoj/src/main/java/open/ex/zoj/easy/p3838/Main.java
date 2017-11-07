package open.ex.zoj.easy.p3838;

/*
 * 
 * Infusion Altar
 Time Limit: 2 Seconds      Memory Limit: 65536 KB
 Bob is recently playing a game called Minecraft, especially a mod called Thaumcraft. It is a mod of magic.

 Usually, Bob has Obsessions with Symmetry while playing Minecraft. This obsession is useless in the gameplay generally. 
 However, in Thaumcraft, the infusion altar requires symmetry to keep it stable.

 Bob built an infusion altar in his secret chamber, but it was not so symmetrical. 
 After some explosions, Bob decided to fix the infusion altar to make it symmetrical.

 InfusionAltar
 You will be given the map of Bob's secret chamber. It is of size n*n(n is an odd number), 
 the infusion altar is always at the center of his secret chamber. The following picture is a typical map. 
 The 3*3 square in the center is the Infusion Altar, it is a multi-block structure. Here, '#' means Runic Matrix, 
 'o' means Arcane Pedestal, '.' means an empty place, 'a'-'z' means occult paraphernalia(like skulls, crystals and candles) 
 Bob placed around the Infusion Altar. There will not be characters other than 'a'-'z', '.', '#'.

 .aab.
 bo.ob
 b.#.a
 bo.ob
 bbab.
 Now, the question is that at least how many blocks need to be changed to make the whole map symmetrical. 
 Here, being symmetrical means having all four axes of symmetry for a square. 
 Also, you can change any character on the map to any other character.

 Input

 There are multiple cases. The first line contains one integer T which is the number of test cases.
 For each case, The first line contains an integer n ( 3 ≤ n ≤ 99, and n is an odd number)
 For the next n lines, each line contains n characters showing the map.
 It is guaranteed that the Infusion Altar is at the center of the map. 
 It is guaranteed that only 'a'-'z' and '.' will appear out of the Infusion Altar.

 Output

 One integer for each test case which is the least number of blocks that should be changed.

 Sample Input

 3
 3
 o.o
 .#.
 o.o
 5
 .aab.
 bo.ob
 b.#.a
 bo.ob
 bbab.
 5
 aabba
 ao.oa
 a.#.a
 ao.oa
 aaaaa
 Sample Output

 0
 3
 2
 Hint

 The first sample is a standard Infusion Altar.
 In second sample, Bob will change his secret chamber to the following map.

 .bab.
 bo.ob
 a.#.a
 bo.ob
 .bab.
 * 
 */
import java.util.Scanner;


/**
 * 
 * 最少经过多少步骤使得棋盘上的棋子是互相对称的？
 * 
 * 对任意一个位置(i,j)找出所有属于一个对称集合的位置，{ix,iy|0<x<N,0<y<N}，
 * 这个集合中所有位置所放置的棋子必须相同才能保持对称。 假设这个集合总共有 sn个位置，
 * 每个位置随机放置a-z和.这27种棋子，假设其中某个棋子使用的数量最多，为sc，那么把剩下的sn-sc
 * 个棋子都替换为c可以达到对称状态。这样是最少的替换数量，另外这种替换和不属于这个集合
 * 的其他位置的状态毫无关联。所以使用贪心算法能够达到最优解。
 * 
 * 对于每个位置(i,j)，都重复上面的操作，就能使得所有位置都对称。
 * 
 * 
 * 
 * @author huash06
 *
 */
public class Main {

	public static int MAX_N = 100;
	public static int COUNT_N = 30;
	public static int N;
	public static int T;
	public static int[][] M = new int[MAX_N][MAX_N];
	public static int[][] SM = new int[MAX_N][MAX_N];
	public static int[] COUNT = new int[COUNT_N];

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		T = scanner.nextInt();
		for (int ti = 0; ti < T; ti++) {
			N = scanner.nextInt();
			scanner.nextLine();
			getInput(scanner);
			initSM();
			System.out.println(count());

		}
		scanner.close();
	}

	public static void getInput(Scanner scanner) {
		for (int i = 0; i < N; i++) {
			char[] line = scanner.nextLine().toCharArray();
			for (int j = 0; j < N; j++) {
				char ch = line[j];
				switch (ch) {
				case '.':
					M[i][j] = 27;
					break;
				case '#':
					M[i][j] = 0;
					break;
				default:
					M[i][j] = ch - 'a' + 1;
				}
			}
		}
	}

	/**
	 * 
	 * Take symmetry into account, we just need count "set" start with left-top 1/4 of the table.
	 * 
	 * @return minimum count of replacement
	 */
	public static int count() {
		int c = 0;
		for (int i = 0; i <= N / 2; i++) {
			for (int j = 0; j <= N / 2; j++) {
				if (M[i][j] > 0) {
					c += count(i, j);
				}
			}
		}
		return c;
	}

	/**
	 * 
	 * Count minimum replacement in set start with (i,j).
	 * 
	 * @param ci
	 * @param cj
	 * @return
	 */
	public static int count(int ci, int cj) {
		for (int i = 0; i < COUNT_N; i++) {
			COUNT[i] = 0;
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (SM[i][j] == SM[ci][cj]) {
					COUNT[M[i][j]]++;
					M[i][j] = -1;
				}
			}
		}
		int tc = 0;
		int mc = -1;
		for (int i = 0; i < COUNT_N; i++) {
			tc += COUNT[i];
			mc = mc > COUNT[i] ? mc : COUNT[i];
		}
		return tc - mc;
	}

	/**
	 * 
	 * initialize an reference table, in which all items are symmetrical.
	 * 
	 */
	public static void initSM() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				SM[i][j] = 0;
			}
		}
		int v = 1;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (SM[i][j] == 0) {
					findSym(i, j, v++);
				}
			}
		}
	}

	/**
	 * 
	 * Mark all location should be symmetrical with same number.
	 * We call the locations with same mark a "set".
	 * The items in same set are symmetrical.
	 * 
	 * @param i row location
	 * @param j column location
	 * @param v mark value
	 */
	public static void findSym(int i, int j, int v) {
		if (SM[i][j] == v) {
			return;
		}
		SM[i][j] = v;
		// horizontal axis
		findSym(N - i - 1, j, v);
		// vertical axis
		findSym(i, N - 1 - j, v);
		// slash
		findSym(N - 1 - i, N - 1 - j, v);
		findSym(j, i, v);
		findSym(N - j - 1, N - i - 1, v);
	}

	public static void outputSm() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				System.out.print(SM[i][j] + " ");
			}
			System.out.println();
		}
	}

}
