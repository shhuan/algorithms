package open.ex.zoj.dp.p1100;

import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Random;

public class CaseGenerator {

	public static void main(String[] args) {
		try {
			System.setOut(new PrintStream("C:\\Users\\huash06\\git\\Algorithms\\zoj\\input_1100.txt"));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		Random rand = new Random();
		for(int i=0; i<100; i++){
			System.out.println((rand.nextInt(11)+1)+" "+(rand.nextInt(11)+1));
		}
		System.out.println("0 0");

	}

}
