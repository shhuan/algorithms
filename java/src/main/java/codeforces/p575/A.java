package codeforces.p575;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Created by huangshuangquan on 2015/9/8.
 */
public class A {
    static int K, P, M, N;
    static int[] S;
    static Map<Integer, Integer> outliers = new HashMap<>();
    public static void main(String[] args) {
        readInput();
        System.out.println(solve());
    }
    static void readInput() {
        Scanner scanner = new Scanner(System.in);
        K = scanner.nextInt();
        P = scanner.nextInt();
        N = scanner.nextInt();
        S = new int[N];
        for (int i = 0; i < N; i++) {
            S[i] = scanner.nextInt();
        }
        M = scanner.nextInt();
        for (int i = 0; i < M; i++) {
            int k = scanner.nextInt();
            int v = scanner.nextInt();
            outliers.put(k, v);
        }
    }
    static int solve() {
        int k0 = 0;
        int k1 = 1;
        if (K == 0) {
            return 0;
        } else if (K == 1) {
            return 1;
        }
        int k2 = 0;
        for (int i = 2; i <= K; i++) {
            k2 = getSi(i-2) * k0 + getSi(i-1) * k1;
            System.err.println(k2);
            k0 = k1;
            k1 = k2;
        }
        return k2 % P;
    }
    static int getSi(int i) {
        if (outliers.containsKey(i)) {
            int result = outliers.get(i);
            outliers.remove(i);
            return result;
        }
        return S[i % N];
    }
}
