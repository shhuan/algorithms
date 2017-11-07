package open.ex.zoj.mid.p3836;

import java.util.Scanner;

/*
 * 
 * 题意：有L个盒子[0..L-1]，每K秒在0号盒子放入一件物品，
每一秒盒子里的物品向前移动一格，到最右边或最左边，
物品反向运动，问最短多少时间内某个盒子中物品数量超过C。


设正向移动且位置在a的盒子已经运动的时间为T1，
逆向移动且位置在a的盒子已经运动的时间为T2。

1) T1 ∈ {a, a+T, a+2T, ..., a+i*T}; T=2(L-1)， 即T1的可能的值是a+i*T
2) T2 ∈ {T-a, 2T-a, ..., i*T-a}; T=2(L-1)
3) 某个盒子一次移动到a时，其他在位置a的盒子运动的时间为t，
   ，那么 (t-a)%K=0, 因为每隔K秒加入一个盒子。
   所以正向移动且在位置a的盒子的运动时间为 a, a+i1*K, a+i2*K, ..., a+in*K
4) 由1和3得出，位置a的盒子的运动时间a加T,K的最小公倍数的倍数，即a+i*T*K/gcd(T,K)
5) 同样的反向移动且位置在a的盒子的运行时间是 b+i*T*K/gcd(T,K),
   由2得出b=x*T-a，由3得出(b-a)%K=0，隐含条件b>a。（中国剩余定理）
6) 大于c个 那么最少要在第几秒 (b无解，或者a==0||a==l-1自行考虑)
    1个是a秒 
    2个是b秒,
    3个是a+T*k/gcd(T,k)秒
    4个是b+T*k/gcd(T,k)秒… 知道规律了
7) 枚举每一个a位置求出这个位置出现大于c个球的最短时间，取最小的一个就可以了。


结论


f(C,a) = a+T*K/gcd(T,K)*C/2, C是奇数
f(C,a) = b+T*K/gcd(T,K)*(C/2-1), C是偶数
b=x*T-a,(b-a)%K=0,b>a
 * 
 * f(C,a) = a+T*K/gcd(T,K)*C/2, C是奇数, T=2(L-1)
 * f(C,a) = b+T*K/gcd(T,K)*(C/2-1), C是偶数
 * b=x*T-a,(b-a)%K=0,b>a
 * 
 * 
 */
public class Main {

	public static Long L, K, C;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (sc.hasNext()) {
			L = sc.nextLong();
			K = sc.nextLong();
			C = sc.nextLong();
			System.out.println(cal());
		}
		sc.close();

	}

	public static Long cal() {
		if (L == 1) {
			return C * K;
		}
		Long t = Long.MAX_VALUE;
		C += 1;
		for (Long i = 0L; i < L; i++) {
			Long tt = f(C, i);
			t = t < tt ? t : tt;
		}
		return t;
	}

	private static Long f(Long c, Long a) {
		Long T = 2 * (L - 1);
		if (a == 0 || a == L - 1)
			return (c - 1) * T + a;
		Long b = fb(a, T, K);
		if (b == -1L) {
			return (c - 1) * T + a;
		}
		if ((c & 1) == 0) {
			return b + T * K / gcd(T, K) * (c / 2 - 1);
		} else {
			return a + T * K / gcd(T, K) * c / 2;
		}
	}

	private static Long fb(Long a, Long t, Long k) {// b=x*t-a,(b-a)%k=0,b>a
		if ((2 * a) % gcd(t, k) != 0) {
			return -1L;
		}
		Long b = (2 * a / t + 1) * t - a;
		while (true) {
			if (((b - a) % k) == 0) {
				break;
			}
			b += t;
		}
		return b;
	}

	private static Long gcd(Long a, Long b) {
		if (a < b) {
			return gcd(b, a);
		}
		Long c = a % b;
		if (c == 0) {
			return b;
		} else {
			return gcd(b, c);
		}
	}

}
