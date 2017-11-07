package open.ex.zoj.dp.p1368;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * @author huash06
 *
 *
 *f(i,j,k)=p表示前i天（包括i），租给前j个人（1<=j<=N,包括j）个人中
 *的某些人后，第0到k天都租出去了，第k+1天开始船空闲（0<=k<=i)，
 *此时获得的收益为p。
 *
 *f*i,j,k)=
 *
 */
public class Main {

	public static int N;//N个客户
	public static int M;//M个选择
	public static int D;//最后一天
	
	public static int MAXN = 101;
	public static int MAXD = 101;
	public static int F[][][] = new int[MAXD][MAXN][MAXD];
	
	public static Map<Integer, List<Choice>> C = new HashMap<>();
	public static int R[] = new int[MAXN];
	
	public static InputStream input;
	public static boolean ONLINE_JUDGE = false;
	public static void main(String[] args) {
		if(ONLINE_JUDGE){
			input = System.in;
		}else{
			input = Main.class.getClassLoader().getResourceAsStream("input_1368.txt");
		}
		Scanner scanner = new Scanner(input);
		int caseIndex = 0;
		while(scanner.hasNextInt()){
			N = scanner.nextInt();
			for(int i=1; i<=N; i++){
				R[i] = scanner.nextInt();
			}
			M = scanner.nextInt();
			C.clear();
			D = 0;
			for(int i=0; i<M; i++){
				int ci = scanner.nextInt();
				int deadline = scanner.nextInt();
				int profit = scanner.nextInt();
				List<Choice> cs = C.get(ci);
				if(cs==null){
					cs = new ArrayList<>();
					C.put(ci, cs);
				}
				cs.add(new Choice(deadline,profit));
				D = D>deadline?D:deadline;
			}
			if(caseIndex>0){
				System.out.println();
			}
			caseIndex++;
			cal();
		}
		
		scanner.close();

	}
	
	public static void cal(){
		dp();
		int p = -1;
		for(int k=0; k<=D; k++){
			p = p>F[D][N][k]?p:F[D][N][k];
		}
		System.out.println(p);
	}
	
	public static void dp(){
		for(int i=0; i<D; i++){
			for(int j=0; j<N; j++){
				for(int k=0; k<D; k++){
					F[i][j][k] = j==0?0:-1;
				}
			}
		}
		
		for(int i=0; i<=D; i++){//前i天，包括i
			for(int j=1; j<=N; j++){//租个前j个（包括j）客户，j=0表示不租给任何客户
				for(int k=0; k<=i; k++){//截止日期是k，船从第k+1天开始空闲可租
					int p = F[i][j-1][k];//不租给客户j
					
					//租给客户j
					if(k>0){
						p = p>F[i][j][k-1]?p:F[i][j][k-1];
					}
					List<Choice> cs = C.get(j);
					for(Choice c : cs){
						if(c.deadline>=k){
							int mk = k-R[j];
							if(mk==-1){//只能租个客户j一个人
								p = p>c.profit?p:c.profit;
							}else{
								for(int k1=mk; k1>=0; k1--){
									if(F[i][j-1][k1]>=0){
										p = p>F[i][j-1][k1]+c.profit?p:F[i][j-1][k1]+c.profit;
									}else{
										break;
									}
								}
							}
							
						}
					}
					F[i][j][k] = p;
//					if(p>=0){
//						System.out.println("f("+i+","+j+","+k+")="+p);
//					}
				}
			}
		}
	}

}
class Choice{
	public int deadline;
	public int profit;
	public Choice(int deadline, int profit) {
		super();
		this.deadline = deadline;
		this.profit = profit;
	}
}
