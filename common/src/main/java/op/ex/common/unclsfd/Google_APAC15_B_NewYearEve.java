package op.ex.common.unclsfd;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

/**
 * @author huash
 *
 *         新年的时候把酒杯堆成金字塔形状，然后从顶部往下倒酒，计算倒完B瓶酒之后第L层第N个酒杯里面有多少酒。
 *
 *
 *         所有酒都倒入了最上面的一个杯子，杯子装不下的部分被平均装入了它下面的三个杯子中，依次递推即可。 不要尝试模拟。
 *         Java中使用数组比Map快很多，大概是5s VS 3s，但是在Python中明显使用dict更快，不过也需要超过20s
 *
 *
 */
public class Google_APAC15_B_NewYearEve {
	public static boolean ONLINE_JUDGE = false;

	public static int Row[] = new int[100000]; // 400*400
	public static int Col[] = new int[100000];
	public static int Num[][] = new int[455][455];

	// Count[level][row][col][0] means the quantity of cup at level, row, col
	// Count[level][row][col][1] means the overflowed quantity of cup at level,
	// row, col
	// cost < 4s
	public static double[][][][] Count = new double[2][455][455][2];

	// cost > 50s
	// public static Map<CupPosition, Status> STATUS = new TreeMap<>();

	// cost > 5s
	public static Map<CupPosition, Status> STATUS = new HashMap<>();

	public static void main(String[] args) {
		if (!ONLINE_JUDGE) {
			System.setIn(Google_MineSweeper.class.getClassLoader().getResourceAsStream("NewYearEve.in"));
			try {
				String op = Google_MineSweeper.class.getClassLoader().getResource("").getPath() + "NewYearEve.out";
				System.err.println(op);
				System.setOut(new PrintStream(new FileOutputStream(op)));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}

		long startTime = new Date().getTime();
		int num = 1;
		for (int row = 1; row <= 400; row++) {
			for (int col = 1; col <= row; col++) {// number of cups on row {row}
													// is {row}
				Row[num] = row;
				Col[num] = col;
				Num[row][col] = num;
				num++;
			}
		}

		Scanner scanner = new Scanner(System.in);
		int T = scanner.nextInt();
		for (int ti = 1; ti <= T; ti++) {
			int B = scanner.nextInt();
			int L = scanner.nextInt();
			int N = scanner.nextInt();
			for (int level = 0; level < 2; level++) {
				// number of rows in level {level} is {level}
				for (int row = 0; row < 455; row++) {
					for (int col = 0; col < 455; col++) {
						Count[level][row][col][0] = 0.0;
						Count[level][row][col][1] = 0.0;
					}
				}
			}
			Count[1][1][1] = new double[] { 250.0, 750.0 * B - 250.0 };
			// STATUS.clear();
			// STATUS.put(new CupPosition(1, 1, 1), new Status(250.0,
			// 750.0*B-250.0));

			for (int level = 1; level <= L; level++) {
				// reset next level before calculate because of previous use
				for (int row = 1; row < 455; row++) {
					for (int col = 1; col < 455; col++) {
						Count[(level + 1) % 2][row][col][0] = 0.0;
						Count[(level + 1) % 2][row][col][1] = 0.0;
					}
				}
				for (int row = 1; row <= level; row++) {
					for (int col = 1; col <= row; col++) {
						double[] rc = Count[level % 2][row][col];
						if (rc[1] > 0.0) {
							rc[0] += rc[1];
							rc[1] = Math.max(rc[0] - 250.0, 0);
							rc[0] = Math.min(250, rc[0]);
						}
						double r = rc[1];
						Count[(level + 1) % 2][row][col][1] += r / 3.0;
						Count[(level + 1) % 2][row + 1][col][1] += r / 3.0;
						Count[(level + 1) % 2][row + 1][col + 1][1] += r / 3.0;
						// CupPosition cp = new CupPosition(level, row, col);
						// Status rc = STATUS.get(cp);
						// if(rc.redundant>0.0){
						// rc.quantity += rc.redundant;
						// rc.redundant = Math.max(0.0, rc.quantity-250.0);
						// rc.quantity = Math.min(250.0, rc.quantity);
						// }
						// CupPosition[] blowCups = new CupPosition[]{
						// new CupPosition(level+1, row, col),
						// new CupPosition(level+1, row+1, col),
						// new CupPosition(level+1, row+1, col+1)
						// } ;
						// for(int i=0;i<blowCups.length; i++){
						// CupPosition p = blowCups[i];
						// Status s = STATUS.get(p);
						// if(s == null){
						// s = new Status(0.0, 0.0);
						// STATUS.put(p, s);
						// }
						// s.redundant += rc.redundant/3.0;
						// }
						// very significant impact on performance
						// STATUS.remove(cp);

					}
				}
			}
			double[] rc = Count[L % 2][Row[N]][Col[N]];
			System.out.println(String.format("Case #%d: %.7f", ti, Math.min(rc[0] + rc[1], 250.0)));
			// Status s = STATUS.get(new CupPosition(L, Row[N], Col[N]));
			// if(s==null){
			// System.out.println(String.format("Case #%d: %.7f", ti, 0.0));
			// }else{
			// System.out.println(String.format("Case #%d: %.7f", ti,
			// Math.min(s.quantity+s.redundant, 250.0)));
			// }

		}
		System.err.println("time cost: " + (new Date().getTime() - startTime));
		scanner.close();
	}
}

class Status {
	double quantity;
	double redundant;

	public Status(double quantity, double redundant) {
		super();
		this.quantity = quantity;
		this.redundant = redundant;
	}

}

class CupPosition implements Comparable<CupPosition> {
	int level;
	int row;
	int col;

	public CupPosition(int level, int row, int col) {
		super();
		this.level = level;
		this.row = row;
		this.col = col;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + col;
		result = prime * result + level;
		result = prime * result + row;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		CupPosition other = (CupPosition) obj;
		if (col != other.col)
			return false;
		if (level != other.level)
			return false;
		if (row != other.row)
			return false;
		return true;
	}

	@Override
	public int compareTo(CupPosition oc) {
		if (oc.level != this.level) {
			return oc.level - this.level;
		} else if (oc.row != this.row) {
			return oc.row - this.row;
		} else {
			return oc.col - this.col;
		}
	}

}
