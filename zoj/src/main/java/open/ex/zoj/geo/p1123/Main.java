package open.ex.zoj.geo.p1123;

import java.util.Scanner;

/**
 * @author huash06
 *
 *         题意： 按照指定格式输出所有在给定三角形内部的点
 * 
 *         分析： 計算點是否在三角形內部
 */
public class Main {

	public static boolean ONLINE_JUDGE = true;

	public static int MAXN = 20;
	public static boolean[][] M = new boolean[MAXN][MAXN];

	public static void main(String[] args) {
		if (!ONLINE_JUDGE) {
			System.setIn(Main.class.getClassLoader().getResourceAsStream("input_1123.txt"));
			// try {
			// System.setOut(new PrintStream(new
			// FileOutputStream(Main.class.getClassLoader().getResource("")
			// .getPath()
			// + "/output_1123.txt")));
			// } catch (FileNotFoundException e) {
			// e.printStackTrace();
			// }
		}
		System.out.println("Program 4 by team X");
		Scanner scanner = new Scanner(System.in);
		while (scanner.hasNextInt()) {
			int vx1 = scanner.nextInt();
			int vy1 = scanner.nextInt();
			int vx2 = scanner.nextInt();
			int vy2 = scanner.nextInt();
			int vx3 = scanner.nextInt();
			int vy3 = scanner.nextInt();

			Vector3i A = new Vector3i(vx1, vy1, 0);
			Vector3i B = new Vector3i(vx2, vy2, 0);
			Vector3i C = new Vector3i(vx3, vy3, 0);

			int minX = Math.min(vx1, Math.min(vx2, vx3));
			int maxX = Math.max(vx1, Math.max(vx2, vx3));
			int minY = Math.min(vy1, Math.min(vy2, vy3));
			int maxY = Math.max(vy1, Math.max(vy2, vy3));

			for (int i = 0; i < MAXN; i++) {
				for (int j = 0; j < MAXN; j++) {
					M[i][j] = false;
				}
			}

			int startX = MAXN;
			int startY = 0;
			for (int x = minX; x <= maxX; x++) {
				for (int y = minY; y <= maxY; y++) {
					Vector3i P = new Vector3i(x, y, 0);
					if (Vector3i.pointInTriangle(A, B, C, P)) {
						M[x - minX][y - minY] = true;
						startX = Math.min(startX, x - minX);
						startY = Math.max(startY, y - minY);
					}
				}
			}
			for (int y = startY; y >= 0; y--) {
				// System.out.println("12345678901234567890123456789012345678901234567890");
				boolean exists = false;
				for (int x = startX; x <= maxX - minX; x++) {
					if (M[x][y]) {
						exists = true;
						if (x > startX) {
							System.out.print(" ");
						}
						System.out.print("(" + String.format("%2d", x + minX) + ", " + String.format("%2d", y + minY)
								+ ")");
					} else {
						boolean hasNext = false;
						for (int xi = x + 1; xi <= maxX - minX; xi++) {
							if (M[xi][y]) {
								hasNext = true;
								break;
							}
						}
						if (hasNext) {
							if (x > startX) {
								System.out.print("         ");
							} else {
								System.out.print("        ");
							}
						} else {
							break;
						}
					}
				}
				if (exists || y == 0) {
					System.out.println();
				}
			}
		}
		System.out.println("End of program 4 by team X");
		scanner.close();

	}

	/**
	 * 
	 * 三角形的三个点在同一个平面上，如果选中其中一个点，其他两个点不过是相对该点的位移而已，比如选择点A作为起点，
	 * 那么点B相当于在AB方向移动一段距离得到，而点C相当于在AC方向移动一段距离得到。
	 * 
	 * 
	 * 
	 * 所以对于平面内任意一点，都可以由如下方程来表示
	 * 
	 * P = A + u * (C – A) + v * (B - A) // 方程1
	 * 
	 * 如果系数u或v为负值，那么相当于朝相反的方向移动，即BA或CA方向。那么如果想让P位于三角形ABC内部，u和v必须满足什么条件呢？有如下三个条件
	 * 
	 * u >= 0
	 * 
	 * v >= 0
	 * 
	 * u + v <= 1
	 * 
	 * 几个边界情况，当u = 0且v = 0时，就是点A，当u = 0,v = 1时，就是点B，而当u = 1, v = 0时，就是点C
	 * 
	 * 整理方程1得到P – A = u(C - A) + v(B - A)
	 * 
	 * 令v0 = C – A, v1 = B – A, v2 = P – A，则v2 = u * v0 + v *v1，
	 * 现在是一个方程，两个未知数，无法解出u和v，将等式两边分别点乘v0和v1的到两个等式
	 * 
	 * (v2) • v0 = (u * v0 + v * v1) • v0
	 * 
	 * (v2) • v1 = (u * v0 + v * v1) • v1
	 * 
	 * 注意到这里u和v是数，而v0，v1和v2是向量，所以可以将点积展开得到下面的式子。
	 * 
	 * v2 • v0 = u * (v0 • v0) + v * (v1 • v0) // 式1
	 * 
	 * v2 • v1 = u * (v0 • v1) + v * (v1• v1) // 式2
	 * 
	 * 解这个方程得到
	 * 
	 * u = ((v1•v1)(v2•v0)-(v1•v0)(v2•v1)) / ((v0•v0)(v1•v1) - (v0•v1)(v1•v0))
	 * 
	 * v = ((v0•v0)(v2•v1)-(v0•v1)(v2•v0)) / ((v0•v0)(v1•v1) - (v0•v1)(v1•v0))
	 * 
	 * @param A
	 * @param B
	 * @param C
	 * @param P
	 * @return 由于精度问题， 这个方法不是非常准确 点(-6, 3) (-5, 3) (-4, 3) (-3, 3)在三角形-7 -1 -2 3
	 *         -7 3的边上，但是返回true
	 * 
	 */
	public static boolean pointInTriangle(Vector3i A, Vector3i B, Vector3i C, Vector3i P) {
		Vector3i v0 = C.sub(A);
		Vector3i v1 = B.sub(A);
		Vector3i v2 = P.sub(A);

		int dot00 = v0.dot(v0);
		int dot01 = v0.dot(v1);
		int dot02 = v0.dot(v2);
		int dot11 = v1.dot(v1);
		int dot12 = v1.dot(v2);

		float inverDeno = 1.0f / (dot00 * dot11 - dot01 * dot01);
		float u = (dot11 * dot02 - dot01 * dot12) * inverDeno;
		if (u <= 0 || u >= 1) // if u out of range, return directly
		{
			return false;
		}

		float v = (dot00 * dot12 - dot01 * dot02) * inverDeno;
		if (v <= 0 || v >= 1) // if v out of range, return directly
		{
			return false;
		}

		return u + v < 1;
	}

}

class Vector3i {
	public int x;
	public int y;
	public int z;

	public Vector3i(int x, int y, int z) {
		super();
		this.x = x;
		this.y = y;
		this.z = z;
	}

	Vector3i sub(Vector3i v) {
		return new Vector3i(x - v.x, y - v.y, z - v.z);
	}

	int dot(Vector3i v) {
		return x * v.x + y * v.y + z * v.z;
	}

	Vector3i cross(Vector3i v) {
		return new Vector3i(y * v.z - z * v.y, z * v.x - x * v.z, x * v.y - y * v.x);
	}

	/**
	 * 
	 * 假设点P位于三角形内，会有这样一个规律，当我们沿着ABCA的方向在三条边上行走时，你会发现点P始终位于边AB，BC和CA的右侧。我们就利用这一点，
	 * 但是如何判断一个点在线段的左侧还是右侧呢？我们可以从另一个角度来思考
	 * ，当选定线段AB时，点C位于AB的右侧，同理选定BC时，点A位于BC的右侧，最后选定CA时
	 * ，点B位于CA的右侧，所以当选择某一条边时，我们只需验证点P与该边所对的点在同一侧即可
	 * 。问题又来了，如何判断两个点在某条线段的同一侧呢？可以通过叉积来实现
	 * ，连接PA，将PA和AB做叉积，再将CA和AB做叉积，如果两个叉积的结果方向一致
	 * ，那么两个点在同一测。判断两个向量的是否同向可以用点积实现，如果点积大于0，则两向量夹角是锐角，否则是钝角。
	 * 
	 * @param A
	 * @param B
	 * @param C
	 * @param P
	 * @return
	 */
	public static boolean sameSide(Vector3i A, Vector3i B, Vector3i C, Vector3i P) {
		Vector3i AB = B.sub(A);
		Vector3i AC = C.sub(A);
		Vector3i AP = P.sub(A);

		Vector3i v1 = AB.cross(AC);
		Vector3i v2 = AB.cross(AP);

		// v1 and v2 should point to the same direction
		return v1.dot(v2) > 0;
	}

	public static boolean pointInTriangle(Vector3i A, Vector3i B, Vector3i C, Vector3i P) {
		return sameSide(A, B, C, P) && sameSide(B, C, A, P) && sameSide(C, A, B, P);
	}

	@Override
	public String toString() {
		return "Vector3i [x=" + x + ", y=" + y + ", z=" + z + "]";
	}
}
