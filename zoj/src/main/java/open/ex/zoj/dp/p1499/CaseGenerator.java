package open.ex.zoj.dp.p1499;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class CaseGenerator {

	public static void main(String[] args) {
		
		try {
			FileWriter fw = new FileWriter("input_1499.txt");
			for(int i=0; i<10000; i++){
				String cs = genCase();
				if(cs.equalsIgnoreCase("0")){
					continue;
				}
				System.out.println(cs);
				fw.write(cs+"\r\n");
			}
			fw.write("0\r\n");
			fw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static String genCase(){
		Random rand = new Random();
		int len = rand.nextInt(80)+1;
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<len; i++){
			int val = rand.nextInt(10);
			sb.append(String.valueOf(val));
		}
		return sb.toString();
	}

}
