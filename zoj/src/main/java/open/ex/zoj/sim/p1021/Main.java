package open.ex.zoj.sim.p1021;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

/**
 * @author huash06
 *
 *
 *
 *	最高位置是y坐标最小的位置
 */
public class Main {

	public static int T;
	public static int MAXN=21;	
//	public static int[][] LINKS = new int[MAXN][MAXN];//LINKS[i][j]=k means pipe i and pipe j linked at height k
	public static Map<Integer,List<Point2D>> LINKS = new HashMap<>();//LINKS[x1] = [[x2,y2],[x3,y3]], means pipe at x1 links pipe at x2 at y, links x3 at y3
	
	public static Map<Point2D, Integer> LKS = new HashMap<>();
	
	public static boolean ONLINE_JUDGE = true;
	public static void main(String[] args) {
		if(!ONLINE_JUDGE){		
			
//	        System.setIn(Main.class.getClassLoader().getResourceAsStream("input_1021.txt"));  
	        
			try {
				InputStream input  = new FileInputStream("C:\\Users\\huash06\\git\\Algorithms\\zoj\\input_1021.txt");
				System.setIn(input);
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
			
			PrintStream ps;
			try {
				ps = new PrintStream(new FileOutputStream("output_1021_java.txt"));
		        System.setOut(ps); 
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}  
		}
		Scanner scanner = new Scanner(System.in);
		T = scanner.nextInt();
		int ti = 0;
		while(T-->0){
			int N = scanner.nextInt();
			List<Pipe> pipes = new ArrayList<Pipe>(N);
			int x,y,h,len;
			for(int i=0; i<N; i++){
				x = scanner.nextInt();
				y = scanner.nextInt();
				h = scanner.nextInt();
				pipes.add(new Pipe(new Point2D(x,y),h,y+h));
			}
			int M = scanner.nextInt();
			
			LINKS.clear();
			for(int i=0; i<M; i++){
				x = scanner.nextInt();
				y = scanner.nextInt();
				len = scanner.nextInt();
				List<Point2D> lk = LINKS.get(x-1);
				if(lk==null){
					lk = new ArrayList<>();
					LINKS.put(x-1, lk);
				}
				lk.add(new Point2D(x+len, y));
				LKS.put(new Point2D(x-1, y), x+len);
			}
			
			for(List<Point2D> lk : LINKS.values()){
				Collections.sort(lk, new Comparator<Point2D>(){
					@Override
					public int compare(Point2D o1, Point2D o2) {
						return o1.x - o2.x;
					}});
			}
			x = scanner.nextInt();
			y = scanner.nextInt();
			Set<Pipe> linkedPipes = new HashSet<Pipe>();
			
			Collections.sort(pipes, new Comparator<Pipe>(){
				@Override
				public int compare(Pipe p1, Pipe p2) {
					return p1.position.x - p2.position.x;
				}});
			
			Point2D target = new Point2D(pipes.get(x-1).position.x,y);
			Pipe initPipe = pipes.get(0);
			pipes.remove(0);
			linkedPipes.add(initPipe);
			State startState = new State(linkedPipes, initPipe.height+initPipe.position.y, initPipe.position.y);
			
			ti++;
			int t = simulate(startState,target,pipes);
//			int t = qs(pipes, target);
			if(t>0){
				System.out.println(t);
			}else{
				System.out.println("No Solution");
			}
		}		
		scanner.close();

	}
	
	public static int qs(List<Pipe> pipes, Point2D target){
		Queue<Pipe> pipeQueue = new PriorityQueue<>(pipes.size(), new Comparator<Pipe>(){
			@Override
			public int compare(Pipe p1, Pipe p2) {
				return p2.level - p1.level;
			}
			
		});
		pipeQueue.add(pipes.get(0));
		pipes.remove(0);
		int totalTime = 0;
		while(!pipeQueue.isEmpty()){
			Pipe p = pipeQueue.poll();
			if(p.level==p.position.y){
				return -1;//溢出
			}
			
			Integer lx = LKS.get(new Point2D(p.position.x, p.level));
			int pi = -1;
			if(lx!=null){//和坐标为x的管道连接
				for(int i=0; i<pipes.size(); i++){
					if(pipes.get(i).position.x == lx){
						pi = i;
						break;
					}
				}
			}
			if(pi>=0){//把新连接的管道加入已经连接到管道中
				pipeQueue.add(pipes.get(pi));
				pipes.remove(pi);
				pipeQueue.add(p);
			}else if(p.position.x==target.x && p.level==target.y){
				return totalTime;
			}else{
				p.level -= 1;
				totalTime++;
				pipeQueue.add(p);
			}
					
		}
		
		return -1;
	}
	
	public static int simulate(State startState, Point2D target, List<Pipe> pipes){
		Deque<State> q = new ArrayDeque<>();
		q.addFirst(startState);
		int totalTime = 0;
		while(!q.isEmpty()){
			State state = q.getFirst();
			int h=-1; //next height
			Pipe tp = null;
			int lpx = -1;//找到一个管道，它的x坐标是lpx,它是与当前已经连通的管道能够连通的下一个管道（高度最低）
			int mi = -1;
			for(Pipe p : state.linkedPipe){
				mi = mi > p.position.x?mi:p.position.x;
			}
			
			int lh = -1;//lowest h， means max h
			for(Pipe p : state.linkedPipe){
				if(h<p.position.y){//最高水位是当前已经连通的管道中有管道溢出时的高度
					h = p.position.y;	
				}
				lh = lh>p.position.y?lh:p.position.y;
				
				List<Point2D> lks = LINKS.get(p.position.x);
				if(lks!=null){
					for(Point2D lk : lks){
						boolean alreadyLinked = false;
						for(Pipe lp : state.linkedPipe){
							if(lp.position.x == lk.x){
								alreadyLinked = true;
								break;
							}
						}
						if(!alreadyLinked){
							if(h<=lk.y){//最高水位是最低的连通通道的位置
								h = lk.y;
								lpx = lk.x;
							}
						}
					}
				}

				if(p.position.x == target.x){
					if(h<target.y){
						h = target.y;
						tp = p;//最高水位是目标位置
					}
				}else if(h>target.y){
					tp = null;
				}
			}
			
			boolean mh = false;
			if(h<state.maxHeight){
				h = state.maxHeight;
				mh = true;
			}
			totalTime += (state.currentHeight-h)*state.linkedPipe.size();
			if(mh){//或者到达当前能够到达的最高位置
				q.removeFirst();
			}else if(lpx>=0){//到达连通通道
				state.currentHeight = h;
				Set<Pipe> ps = new HashSet<>();
				Pipe np = null;
				for(Pipe p : pipes){
					if(p.position.x == lpx){
						np = p;
						break;
					}
				}
				ps.add(np);
				State s = new State(ps, np.position.y+np.height, h);
				state.linkedPipe.add(np);
				q.addFirst(s);
			}else if(h<=lh){//到达溢出点
				return -1;
			}else if(tp!=null){//到达目标位置
				return totalTime;
			}else{//到达某个水管的最高点
				return -1;
			}
			
		}
		return totalTime;
	}

}

class State{
	public Set<Pipe> linkedPipe;//所有连接到一起的管道
	public int currentHeight;
	public int maxHeight;
	public State(Set<Pipe> linkedPipe, int currentHeight, int maxHeight) {
		super();
		this.linkedPipe = linkedPipe;
		this.currentHeight = currentHeight;
		this.maxHeight = maxHeight;
	}
}

class Pipe{
	public Point2D position;
	public int height;
	public int level;//水位
	public Pipe(Point2D position, int height, int level) {
		super();
		this.position = position;
		this.height = height;
		this.level = level;
	}

}

class Point2D{
	public int x;
	public int y;
	public Point2D(int x, int y) {
		super();
		this.x = x;
		this.y = y;
	}
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + x;
		result = prime * result + y;
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
		Point2D other = (Point2D) obj;
		if (x != other.x)
			return false;
		if (y != other.y)
			return false;
		return true;
	}
}
