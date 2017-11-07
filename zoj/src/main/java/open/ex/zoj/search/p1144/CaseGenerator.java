package open.ex.zoj.search.p1144;

import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Random;

public class CaseGenerator {

	public static void main(String[] args) {
		try {
			System.setOut(new PrintStream(CaseGenerator.class.getClassLoader().getResource("input_1144.txt").getPath()));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		int caseCount = 10;
		for(int i=0; i<caseCount; i++){
			generateCase();
		}
		System.out.println("0 0 0");
	}

	private static void generateCase() {
		Random rand = new Random();
		int W = 10+rand.nextInt(90);
		int H = 10+rand.nextInt(90);
		int T = 3+rand.nextInt(10);
		
		boolean[][][] M = new boolean[T+2][W+2][H+2];
		for(int i=1; i<=T; i++){
			for(int x=1; x<=W; x++){
				for(int y=1; y<=H; y++){
					M[i][x][y] = false;
				}
			}
		}
		int initCount = rand.nextInt(W*5+1)+1;
		for(int i=0; i<initCount; i++){
			int x = 1+rand.nextInt(W);
			int y = 1+rand.nextInt(H);
			M[1][x][y] = true;
		}
		
		for(int t=2; t<T; t++){
			int count = 0;
			for(int x=1; x<=W; x++){
				for(int y=1; y<=H; y++){
					if(M[t-1][x][y]){
						count++;
					}
				}
			}
			if(count<=0){
				break;
			}
			if(t==T-1){
				count = 1;
			}else{
				count = count/2+rand.nextInt(count);
			}
			
			for(int c=0; c<count; c++){
				for(int x=1; x<=W; x++){
					for(int y=1; y<=H; y++){
						if(M[t-1][x][y]){
							M[t][x][y] = true;
							if(rand.nextInt(10)>2){
								M[t][x-1][y] = true;
							}
							if(rand.nextInt(10)>2){
								M[t][x+1][y] = true;
							}
							if(rand.nextInt(10)>2){
								M[t][x][y-1] = true;
							}
							if(rand.nextInt(10)>2){
								M[t][x][y+1] = true;
							}
						}
					}
				}
			}
		}
		
		
		int bc = 1+rand.nextInt(T-2);
		System.out.println(String.format("%d %d %d", W, H, T));
		System.out.println(bc);
		
		boolean[] ts = new boolean[T+1];
		for(int i=1; i<=T; i++){
			ts[i] = true;
		}
		while(true){
			int l = 1+rand.nextInt(T-1);
			ts[l] = false;
			int count = 0;
			for(int i=1; i<T; i++){
				if(ts[i]){
					count++;
				}
			}
			if(count==bc){
				break;
			}
		}
		for(int i=1; i<T; i++){
			if(ts[i]){
				int l=0,b = 0,r = 0,t = 0;
				
				boolean[][] mt = M[i];
				boolean found = false;
				for(l=1; l<W && !found; l++){
					for(r=W; r>l && !found; r--){
						for(b=1; b<H && !found; b++){
							for(t=H; t>b && !found; t--){
								if(notInRect(mt, l, r, b, t)){
									found = true;
								}
							}
						}
					}
				}
				
				System.out.println(String.format("%d %d %d %d %d", i, l, b, r, t));
			}
		}

	}
	
	public static boolean notInRect(boolean[][] M, int l, int r, int b, int t){
		for(int x=l; x<=r; x++){
			for(int y=b; y<=t; y++){
				if(M[x][y]){
					return false;
				}
			}
		}
		return true;
	}
	

}
