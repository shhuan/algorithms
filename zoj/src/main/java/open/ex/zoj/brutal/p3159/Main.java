package open.ex.zoj.brutal.p3159;

import java.util.Scanner;

/**
 * @author huash06
 *
 *
	情人节月老为了让喜鹊组成鹊桥要让大家聚在同一地点开会。假想所有
	喜鹊都在一个二维平面内，且喜鹊在x方向和y方向各有一个速度上限，
	而月老一次只能通知一只喜鹊到指定地点集合，每两次间隔时间t，要
	求聚集所有喜鹊用时最短。
	
	
	显然问题关于时间是满足可二分性的，而确定了时间后，假如再确定了
	月老催每只喜鹊的顺序，那么喜鹊所能到达的区域是一个可简单计算确定
	的边平行于坐标轴的矩形。对于N个这样的矩形判断其是否有公共部分只
	要简单的坐标比较就可以知道了。而公共部分内的点都可以作为集结点。
	所以只要取合适的上下界，二分(即折半查找)时间，枚举所有排列，再判断是否有公共
	部分，然后继续二分，直到满足精度要求为止，输出答案就可以了。
	假设二分的时间为T，月老计划第k个催喜鹊i，则这只喜鹊对应的矩形
	为
	[xi − Vx*t, xi + Vx*t] × [yi − Vy*t, yi + Vy*t], t= max {T − (k − 1)t, 0}.
	如果有
	max xmin ≤ min xmax, max ymin ≤ min ymax
	那么所有矩形交集非空。
	对于枚举所有顺序，C++可以直接利用std::next permutation，而如果
	自己实现的话可以合并公共运算，提前剪枝，速度应该会更快。

 */
public class Main {

	public static double EPS = 1e-8;
	
	public static int N;
	public static int Vx;
	public static int Vy;
	public static int T;
	public static Point[] pt;
	public static boolean ONLINE_JUDGE = true;
	public static void main(String[] args) {
		if(!ONLINE_JUDGE){		
	        System.setIn(Main.class.getClassLoader().getResourceAsStream("input_3159.txt"));
	    }  
	
		Scanner scanner = new Scanner(System.in);
		while(scanner.hasNextInt()){
			N = scanner.nextInt();
			Vx = scanner.nextInt();
			Vy = scanner.nextInt();
			T = scanner.nextInt();
			pt = new Point[N];
			for(int i=0; i<N;i++){
				int x = scanner.nextInt();
				int y = scanner.nextInt();
				pt[i] = new Point(x, y, i);
			}
			cal();
		}
		scanner.close();

	}
	
	public static void cal(){
		double ans = 1e30;
        do
        {
            int cnt = 0;
            double low = 0, high = 1e10;
            //if(chk(high)==false) continue;    high is absolutely ok , not need to check
            while(high - low > EPS && cnt < 100)
            {
                double mid = (high + low)/2;
                if(check(mid))high = mid;
                else low = mid;
                cnt ++;
            }
            ans = Math.min(ans,high);

        }while(nextPermutation(pt));
        System.out.println(ans);
	}


	public static boolean check(double endTime)
	{
	    double xMin = -1e30 , yMin = -1e30;
	    double xMax = 1e30 , yMax = 1e30;
	    double left = endTime;

	    for(int i = 0 ; i < N ; i++)
	    {    
	        double _xMin = pt[i].x - left*Vx , _yMin = pt[i].y - left*Vy;
	        double _xMax = pt[i].x + left*Vx , _yMax = pt[i].y + left*Vy;

	        xMin = Math.max(xMin , _xMin);
	        xMax = Math.min(xMax , _xMax);
	        if(xMin > xMax + EPS)return false;

	        yMin = Math.max(yMin , _yMin);
	        yMax = Math.min(yMax , _yMax);
	        if(yMin > yMax + EPS)return false;

	        left -= T;

	        if(left < 0)left = 0;//需要这样子！！有些鸟可以不用飞出去
	    }
	    return true;
	}
	
	public static void outputArray(int[] arr){
		for(int i=0; i<arr.length; i++){
			System.out.print(arr[i]+" ");
		}
		System.out.println();
	}
	
	public static boolean nextPermutation(Point[] arr){
		if(arr==null || arr.length<=1){
			return false;
		}
		for(int ii=arr.length-1; ii>0; ii--){
			int i = ii-1;
			if(arr[i].id<arr[ii].id){
				int j=arr.length-1;
				for(; j>=0; j--){
					if(arr[i].id<arr[j].id){
						break;
					}
				}
				if(j>0){
					swap(arr, i, j);
					reverse(arr, ii, arr.length-1);
					return true;
				}
			}
		}
		reverse(arr, 0, arr.length-1);
		return false;
	}
	public static void swap(Point[] arr, int swi, int swj){
		Point tmp = arr[swi];
		arr[swi] = arr[swj];
		arr[swj] = tmp;
	}
	public static void reverse(Point[] arr, int ri, int rj){
		while(ri<rj){
			swap(arr, ri, rj);
			ri++;
			rj--;
		}
	}

}

class Point{
	public int x;
	public int y;
	public int id;
	public Point(int x, int y, int id) {
		super();
		this.x = x;
		this.y = y;
		this.id = id;
	}
	
}
