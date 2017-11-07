package open.ex.zoj.sim.p1021;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class CaseGenerator {

	public static void main(String[] args) {
		PrintStream ps;		
		try {
			ps = new PrintStream(new FileOutputStream("input_1021.txt"));
	        System.setOut(ps); 
			int T = 10000;
			System.out.println(T);
			for(int i=0; i<T; i++){
				generateCase();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
	
	public static void generateCase(){
		Random rand = new Random();
		int p = rand.nextInt(5)+1;//number of pipes
		List<Integer> xs = new ArrayList<>();
		for(int i=0; i<p*10; i++){
			xs.add(rand.nextInt(p*4));
		}
		Collections.sort(xs);
		int px = xs.get(0);
		List<Integer> ax = new ArrayList<Integer>();
		for(int i=1; i<xs.size(); i++){
			int x = xs.get(i);
			if(x-px>1){
				ax.add(x);
				px = x;
			}
		}
		if(ax.size()<p){
			generateCase();
			return;
		}
		System.out.println(p);
		List<P> pipes = new ArrayList<P>();
		for(int i=0; i<p; i++){
			int x = ax.get(i);
			int y = rand.nextInt(20);
			int h = rand.nextInt(20)+1;
			pipes.add(new P(x,y,h));
			System.out.println(x+" "+y+" "+h);
		}
		

		int l = rand.nextInt(5);//number of links
		List<L> links = new ArrayList<L>();
		int t = 0;
		for(int i=0; i<l && t<pipes.size()*pipes.size(); t++){
			int a = rand.nextInt(pipes.size());
			if(pipes.size()-a-1<=0){
				continue;
			}
			int b = a+1+rand.nextInt(pipes.size()-a-1);
			P pa = pipes.get(a);
			P pb = pipes.get(b);
			int x = pa.x+1;
			int len = pb.x-pa.x-1;
			int y = -1;
			if(pa.y<=pb.y && pa.y+pa.height>=pb.y){
				int bd = pa.y+pa.height-pb.y;
				y = bd>0?pb.y+rand.nextInt(pa.y+pa.height-pb.y):pb.y;
			}else if(pa.y>pb.y && pa.y<=pb.y+pb.height){
				int bd = pb.y+pb.height-pa.y;
				y = bd>0?pa.y+rand.nextInt(pb.y+pb.height-pa.y):pa.y;
			}
			if(y>=0){
				boolean sameY = false;
				for(L lk : links){
					if(lk.y == y){
						sameY = true;
						break;
					}
				}
				if(sameY || true){
					i++;
					links.add(new L(x,y,len));
				}
			}
		}
		System.out.println(links.size());
		for(L link : links){
			System.out.println(link.x+" "+link.y+" "+link.len);
		}
		
		int ti = rand.nextInt(pipes.size());
		P tp = pipes.get(ti);
		int ty = tp.y+rand.nextInt(tp.height);
		System.out.println((ti+1)+" "+ty);
		System.out.println();
	}

}
class P{
	public int x;
	public int y;
	public int height;
	public P(int x, int y, int height) {
		super();
		this.x = x;
		this.y = y;
		this.height = height;
	}
}
class L{
	public int x;
	public int y;
	public int len;
	public L(int x, int y, int len) {
		super();
		this.x = x;
		this.y = y;
		this.len = len;
	}
}
