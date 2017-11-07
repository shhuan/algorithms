package codeforces.p538b;

import java.io.InputStream;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

	public static void main(String[] args) {

		Main solver = new Main();
		solver.readInput(System.in);
		solver.solve();

	}
	private int N = 0;
	private char[][] boards = null;
	public void readInput(InputStream input){
		Scanner scanner = new Scanner(input);
		this.N = scanner.nextInt();
		scanner.nextLine();
		this.boards = new char[this.N][this.N];
		for(int i=0; i<N; i++){
			String line = scanner.nextLine();
			for(int j=0; j<N; j++){
				this.boards[i][j] = line.charAt(j);
			}
		}
		scanner.close();
	}
	public void solve(){
		class V2{
			public int x;
			public int y;
			public V2(int x, int y) {
				super();
				this.x = x;
				this.y = y;
			}
			public V2 add(V2 other){
				return new V2(this.x+other.x, this.y+other.y);
			}
			public V2 minus(V2 other){
				return new V2(this.x-other.x, this.y-other.y);
			}
			public boolean valid(int N){
				return this.x >= 0 && this.x < N && this.y >= 0 && this.y < N;
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
				V2 other = (V2) obj;
				if (x != other.x)
					return false;
				if (y != other.y)
					return false;
				return true;
			}
		}
		Set<V2> impossibleMoves = new HashSet<>(); 
		Set<V2> chesses = new HashSet<>();
		Set<V2> notAttacked = new HashSet<>();
		
		for(int r=0; r<N; r++){
			for(int c=0; c<N; c++){
				if(this.boards[r][c] == 'o'){
					chesses.add(new V2(r, c));
				}else if(this.boards[r][c] == '.'){
					notAttacked.add(new V2(r, c));
				}
			}
		}
		
		for(V2 rc : chesses){
			for(V2 ij : notAttacked){
				impossibleMoves.add(ij.minus(rc));
			}
		}
		
		for(V2 rc : chesses){
			for(int i=-N+1; i<N; i++){
				for(int j=-N+1; j<N; j++){
					V2 ij = new V2(i, j);
					if(!impossibleMoves.contains(ij)){
						V2 nrc = rc.add(ij);
						if(nrc.valid(N)){
							if(this.boards[nrc.x][nrc.y] == '.'){
								System.out.println("NO");
								return;
							}
							this.boards[nrc.x][nrc.y] = 'v';
						}
					}
				}
			}
		}
		
		for(int i=0; i<N; i++){
			for(int j=0; j<N; j++){
				if(this.boards[i][j] == 'x'){
					System.out.println("NO");
					return;
				}
			}
		}
		
		int rn = N*2 - 1;
		char[][] res = new char[rn][rn];
		for(int i=0; i<rn; i++){
			for(int j=0; j<rn; j++){
				res[i][j] = '.';
			}
		}
		res[N-1][N-1] = 'o';
		for(int i=-N+1; i< N; i++){
			for(int j=-N+1; j<N; j++){
				if(i==0 && j==0){
					continue;
				}
				if(!impossibleMoves.contains(new V2(i, j))){
					res[i+N-1][j+N-1] = 'x';
				}
			}
		}
		System.out.println("YES");
		for(int i=0; i<rn; i++){
			String row = "";
			for(int j=0; j<rn; j++){
				row += res[i][j];
			}
			System.out.println(row);
		}
		
	}

}
