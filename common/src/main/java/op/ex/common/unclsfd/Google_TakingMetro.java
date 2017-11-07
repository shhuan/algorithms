package op.ex.common.unclsfd;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Google_TakingMetro {

	public static boolean ONLINE_JUDGE = false;

	public static int MAX_STAION = 1002;
	public static int MAX_LINE = 102;
	public static int[] StationCount = new int[MAX_LINE];
	public static int N = 0;
	public static int[] WaitTime = new int[MAX_LINE];
	public static int[][] StationTime = new int[MAX_LINE][MAX_STAION];
	public static Map<Position, List<Position>> Transfer = new HashMap<>();
	public static int[][] TravelTime = new int[MAX_LINE][MAX_STAION];

	public static Map<Position, Position> Path = new TreeMap<>();

	public static void main(String[] args) throws IOException {
		if (!ONLINE_JUDGE) {
			System.setIn(Google_TakingMetro.class.getClassLoader().getResourceAsStream("B-small-practice.in"));
			// System.setIn(Google_TakingMetro.class.getClassLoader().getResourceAsStream("sample.txt"));

			try {
				System.setOut(new PrintStream(new FileOutputStream("D:\\tmp\\B-small-practice.out")));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}

		}
		FileWriter pathOut = null;
		try {
			pathOut = new FileWriter("D:\\tmp\\path.txt");
		} catch (IOException e) {
			e.printStackTrace();
		}

		Scanner scanner = new Scanner(System.in);
		int T = scanner.nextInt();
		pathOut.write(T + "\r\n\r\n");
		for (int ti = 1; ti <= T; ti++) {
			System.out.println("Case #" + ti + ":");
			N = scanner.nextInt();

			for (int i = 0; i < MAX_LINE; i++) {
				for (int j = 0; j < MAX_STAION; j++) {
					TravelTime[i][j] = Integer.MAX_VALUE;
					StationTime[i][j] = 0;
				}
				StationCount[i] = 0;
				WaitTime[i] = 0;
			}
			Transfer.clear();

			for (int i = 1; i <= N; i++) {
				StationCount[i] = scanner.nextInt();
				WaitTime[i] = scanner.nextInt();
				for (int j = 1; j < StationCount[i]; j++) {
					StationTime[i][j] = scanner.nextInt();
				}
			}

			int transferCount = scanner.nextInt();
			for (int i = 0; i < transferCount; i++) {
				int startLine = scanner.nextInt();
				int startStation = scanner.nextInt();
				int endLine = scanner.nextInt();
				int endStation = scanner.nextInt();
				int tranferTime = scanner.nextInt();
				Position depart = new Position(startLine, startStation, tranferTime);
				Position dest = new Position(endLine, endStation, tranferTime);
				List<Position> dests = Transfer.get(depart);
				if (dests == null) {
					dests = new ArrayList<>();
					Transfer.put(depart, dests);
				}
				dests.add(dest);
				dests = Transfer.get(dest);
				if (dests == null) {
					dests = new ArrayList<>();
					Transfer.put(dest, dests);
				}
				dests.add(depart);
			}

			int queryCount = scanner.nextInt();
			pathOut.append(queryCount + "\r\n\r\n");
			for (int qi = 0; qi < queryCount; qi++) {
				for (int i = 0; i < MAX_LINE; i++) {
					for (int j = 0; j < MAX_STAION; j++) {
						TravelTime[i][j] = Integer.MAX_VALUE;
					}
				}
				Path.clear();
				int startLine = scanner.nextInt();
				int startStation = scanner.nextInt();
				int endLine = scanner.nextInt();
				int endStation = scanner.nextInt();

				Position startPos = new Position(startLine, startStation, 0);

				// 到达始发站的时间是0
				TravelTime[startLine][startStation] = 0;

				// 从始发站到同一线路的相邻站点，花费时间需要加上等车的时间
				moveOnLine(startPos, true);

				dumpStationTime("D:\\tmp\\Paths\\" + ti + "-" + qi + ".txt");
				dumpPath(pathOut, endLine, endStation);
			}
			pathOut.append("\r\n");

		}
		pathOut.close();
		scanner.close();

	}

	private static void dumpPath(FileWriter pathOut, int endLine, int endStation) throws IOException {
		if (TravelTime[endLine][endStation] < Integer.MAX_VALUE) {
			System.out.println(TravelTime[endLine][endStation]);
			Position pos = new Position(endLine, endStation, 0);
			int count = 0;
			while (pos != null) {
				count++;
				pos = Path.get(pos);
			}

			pathOut.append((count - 1) + "\r\n");
			pos = new Position(endLine, endStation, 0);
			while (pos != null) {
				Position pre = Path.get(pos);
				if (pre != null) {
					pathOut.append(String.format("%d %d %d %d %d\r\n", pre.lineNo, pre.stationNo, pos.lineNo,
							pos.stationNo, TravelTime[pos.lineNo][pos.stationNo]));
				}
				pos = pre;
			}

		} else {
			pathOut.append("0\r\n");
			System.out.println(-1);
		}

	}

	public static void moveOnLine(Position pos, boolean waiting) {
		int waitTime = waiting ? WaitTime[pos.lineNo] : 0;
		// stationNo in [1, N]

		List<Position> updated = new ArrayList<>();
		int nextStationNo = pos.stationNo + 1;
		int cost = TravelTime[pos.lineNo][pos.stationNo] + waitTime;
		while (nextStationNo <= StationCount[pos.lineNo]) {
			cost += StationTime[pos.lineNo][nextStationNo - 1];
			if (cost < TravelTime[pos.lineNo][nextStationNo]) {
				TravelTime[pos.lineNo][nextStationNo] = cost;
				Position dest = new Position(pos.lineNo, nextStationNo, 0);
				Path.put(dest, pos);
				updated.add(dest);
			}
			nextStationNo++;
		}

		nextStationNo = pos.stationNo - 1;
		cost = TravelTime[pos.lineNo][pos.stationNo] + waitTime;
		while (nextStationNo >= 1) {
			cost += StationTime[pos.lineNo][nextStationNo];
			if (cost < TravelTime[pos.lineNo][nextStationNo]) {
				TravelTime[pos.lineNo][nextStationNo] = cost;
				Position dest = new Position(pos.lineNo, nextStationNo, 0);
				Path.put(dest, pos);
				updated.add(dest);
			}
			nextStationNo--;
		}
		transfer(pos);
		for (Position p : updated) {
			transfer(p);
		}
	}

	/**
	 * 
	 * Transfer from pos
	 * 
	 * @param q
	 * @param pos
	 */
	public static boolean transfer(Position pos) {
		if (Transfer.containsKey(pos)) {
			List<Position> transferDests = Transfer.get(pos);
			for (Position tdest : transferDests) {
				int cost = TravelTime[pos.lineNo][pos.stationNo] + tdest.time;

				if (cost < TravelTime[tdest.lineNo][tdest.stationNo]) {
					TravelTime[tdest.lineNo][tdest.stationNo] = cost;
					Position dest = new Position(tdest.lineNo, tdest.stationNo, 0);
					Path.put(dest, pos);
					moveOnLine(dest, true);
				}
			}
			return true;
		}
		return false;
	}

	public static void dumpStationTime(String filePath) {

		FileWriter pathOut = null;
		try {
			pathOut = new FileWriter(filePath);
			for (Position dest : Path.keySet()) {
				Position depart = Path.get(dest);
				pathOut.append(String.format("%d %d %d %d %d\r\n", depart.lineNo, depart.stationNo, dest.lineNo,
						dest.stationNo, TravelTime[dest.lineNo][dest.stationNo]));
			}

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (pathOut != null) {
				try {
					pathOut.close();
				} catch (Exception e) {

				}
			}
		}

	}
}

class Position implements Comparable {
	public int lineNo;
	public int stationNo;
	public int time;

	public Position(int lineNo, int stationNo, int time) {
		super();
		this.lineNo = lineNo;
		this.stationNo = stationNo;
		this.time = time;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + lineNo;
		result = prime * result + stationNo;
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
		Position other = (Position) obj;
		if (lineNo != other.lineNo)
			return false;
		if (stationNo != other.stationNo)
			return false;
		return true;
	}

	@Override
	public int compareTo(Object pos) {
		if (pos instanceof Position) {
			Position p = (Position) pos;
			int ld = lineNo - p.lineNo;
			if (ld == 0) {
				return stationNo - p.stationNo;
			}
			return ld;
		}
		return -1;
	}

}