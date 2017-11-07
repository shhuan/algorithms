package open.ex.zoj.easy.p3840;

/*
 * 
 * 
 * ZOJ Problem Set - 3840
 Nuclear Power Plant
 Time Limit: 2 Seconds      Memory Limit: 65536 KB
 There are N (1 ≤ N ≤ 105) cities on land, and there are N - 1 wires connecting the cities. 
 Therefore, each city can transmit electricity to all other cities by these wires.

 Dark_Sun made a decision to build a nuclear power plant to supply electricity for all the cities. 
 The nuclear power plant can be built in any city, but the cost for the electricity transmission is very strange. 
 Let the weight of wire which connects city u and city v is E(u, v) (|E(u, v)| < 109). 
 If the power plant is built in city x, the cost for electricity transmission from city x to city y is 
 D(x, y) = (E(x, s1) + E(s1, s2) + ... + E(sp, y))k, where {x, s1, s2, ..., sp, y} is the path from x to y. 
 Because of the bug of the computer, the total cost for building a nuclear power plant in city x is 
 Σ(D(x, i)) mod 100000007 (0 ≤ i < N, i ≠ x), and the total cost is obviously not a negative number.

 Dark_Sun asks you to write a program to calculate the minimum total cost.

 Input

 Input will consist of multiple test cases.

 The first line of each test case contains two integers N, K (1 ≤ N ≤ 105,0 ≤ K ≤ 10).

 The next N - 1 lines, each line contains three integers u, v, w (0 ≤ u, v < N, |w| < 109, u ≠ v), indicating E(u, v) is w.

 Output

 For each case, output one line with one integer, indicating the minimum total cost.

 Sample Input

 3 2
 0 1 2
 1 2 2
 Sample Output

 8

 * 
 */

import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	private static int N;
	private static int K;
	private static int MAX_N = 100000;
	private static Map<Path, Integer> E = new HashMap<>(MAX_N*18);
	private static int[] PATH = new int[MAX_N];

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		while (scanner.hasNext()) {
			getInput(scanner);
			System.out.println(minCost());
		}

	}

	public static int minCost() {
		int c = Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			int ci = cost(i);
			c = c > ci ? ci : c;
		}
		return c;
	}

	public static void getInput(Scanner scanner) {
		N = scanner.nextInt();
		K = scanner.nextInt();
		E.clear();
		for (int i = 0; i < N - 1; i++) {
			int ei = scanner.nextInt();
			int ej = scanner.nextInt();
			int w = scanner.nextInt();
			E.put(new Path(ei, ej), w);
			E.put(new Path(ej, ei), w);
		}
	}

	private static void getPath(int plant) {
		Queue<Integer> q = new ArrayDeque<>(MAX_N);
		for (int i = 0; i < N; i++) {
			PATH[i] = Integer.MAX_VALUE;
		}
		PATH[plant] = 0;
		q.add(plant);
		while(q.size()>0){
			int i = q.poll();
			Integer w;
			for(int j=0; j<N; j++){
				w = E.get(new Path(i,j));
				if(w!=null){
					w += PATH[i];
					if(PATH[j]>w){
						PATH[j] = w;
						if(!q.contains(j)){
							q.add(j);
						}
					}
				}
			}
		}
	}

	private static int cost(int plant) {
		getPath(plant);
		int c = 0;
		for (int i = 0; i < N; i++) {
			c += Math.pow(PATH[i], K);
			c = c > 100000007 ? c % 100000007 : c;
		}
		return c;
	}

}

class Path {
	public int i;
	public int j;

	public Path(int i, int j) {
		super();
		this.i = i;
		this.j = j;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + i;
		result = prime * result + j;
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
		Path other = (Path) obj;
		if (i != other.i)
			return false;
		if (j != other.j)
			return false;
		return true;
	}
}