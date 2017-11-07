package open.ex.zoj.geo.p1123;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Random;

public class CaseGenerator {

	public static void main(String[] args) {

		try {
			System.setOut(new PrintStream(new FileOutputStream(CaseGenerator.class.getClassLoader().getResource("")
					.getPath()
					+ "/input_1123.txt")));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		Random rand = new Random();
		for (int i = 0; i < 10000; i++) {
			int x = -10 + rand.nextInt(20);
			int y = -10 + rand.nextInt(20);

			System.out.println(x + " " + y + " " + (x + rand.nextInt(10)) + " " + (y + rand.nextInt(10)) + " "
					+ (x + rand.nextInt(10)) + " " + (y + rand.nextInt(10)));

		}
	}

}
