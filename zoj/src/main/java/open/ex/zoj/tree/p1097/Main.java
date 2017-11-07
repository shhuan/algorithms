package open.ex.zoj.tree.p1097;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;


public class Main {

	public static boolean ONLINE_JUDGE = false;
	public static int MAXN =  51;
	public static int[] V = new int [MAXN];
	public static int[] P = new int [MAXN];
	public static int N;
	public static void main(String[] args) {
		if(!ONLINE_JUDGE){		
	        System.setIn(Main.class.getClassLoader().getResourceAsStream("input_1097.txt"));
	    }  
	
		Scanner scanner = new Scanner(System.in);
		while(scanner.hasNextLine()){
			String line = scanner.nextLine();
			N=0;
			parse(line,0);
			cal();
		}
		scanner.close();
	}
	private static void cal() {
		Map<Integer,List<Integer>> children = new HashMap<>();
		Map<Integer, Node> nodes = new HashMap<>();
		for(int i=0; i<N; i++){
			int p = P[V[i]];
			int v = V[i];
			Node node = new Node(V[i],p);
			List<Integer> c = children.get(p);
			if(c==null){
				c = new ArrayList<Integer>(2);
				children.put(p, c);
			}
			c.add(v);
			nodes.put(v, node);
		}
		
		Queue<Node> q = new PriorityQueue<>(new Comparator<Node>(){
			@Override
			public int compare(Node n1, Node n2) {
				if(n1.children.size()!=n2.children.size()){
					return n1.children.size() - n2.children.size();
				}else{
					return n1.val - n2.val;
				}
			}});
		for(Node node : nodes.values()){
			node.children = children.get(node.val);
			if(node.children==null){
				node.children = new ArrayList<Integer>(1);
			}
			if(node.children.isEmpty()){
				q.add(node);
			}
		}
		List<Integer> result = new ArrayList<Integer>(N);
		while(!q.isEmpty()){
			Node node = q.poll();
			Node parent = nodes.get(node.parent);
			if(parent==null || parent.val<=0){
				continue;
			}
			result.add(node.parent);
			if(parent.children!=null){
				parent.children.remove(parent.children.indexOf(node.val));
			}
			if(parent.children.isEmpty()){
				q.add(parent);
			}
		}
		for(int i=0; i<result.size(); i++){
			System.out.print(result.get(i));
			if(i<result.size()-1){
				System.out.print(" ");
			}
		}
		System.out.println();
	}
	private static void parse(String line, int parent) {
		if(line==null || line.length()<=0){
			return;
		}
		int root = line.charAt(1)-'0';
		V[N++] = root;
		P[root] = parent;
		int parenthesCount = 0;
		int is = 3;
		for(int i=3;i<line.length()-1;i++){
			if(line.charAt(i)=='('){
				parenthesCount++;
			}else if(line.charAt(i)==')'){
				parenthesCount--;
			}
			if(parenthesCount==0 && i+1>is){
				parse(line.substring(is,i+1), root);
				is = i+2;
			}
		}
		
	}

}
class Node{
	int val;
	int parent;
	List<Integer> children;
	public Node(int val, int parent) {
		super();
		this.val = val;
		this.parent = parent;
	}

}