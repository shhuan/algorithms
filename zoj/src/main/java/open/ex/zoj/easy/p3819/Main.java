package open.ex.zoj.easy.p3819;

/*
 * 
 * 
 * Average Score
 Time Limit: 2 Seconds      Memory Limit: 65536 KB
 
 Bob is a freshman in Marjar University. He is clever and diligent. 
 However, he is not good at math, especially in Mathematical Analysis.

 After a mid-term exam, Bob was anxious about his grade. 
 He went to the professor asking about the result of the exam. The professor said:

 "Too bad! You made me so disappointed."

 "Hummm... I am giving lessons to two classes. 
 If you were in the other class, the average scores of both classes will increase."

 Now, you are given the scores of all students in the two classes, except for the Bob's. 
 Please calculate the possible range of Bob's score. All scores shall be integers within [0, 100].

 Input

 There are multiple test cases. The first line of input contains an integer T 
 indicating the number of test cases. For each test case:

 The first line contains two integers N (2 <= N <= 50) and M (1 <= M <= 50) 
 indicating the number of students in Bob's class and the number of students in the other class respectively.

 The next line contains N - 1 integers A1, A2, .., AN-1 representing the scores of other students in Bob's class.

 The last line contains M integers B1, B2, .., BM representing the scores of students in the other class.

 Output

 For each test case, output two integers representing the minimal possible score and the maximal possible score of Bob.

 It is guaranteed that the solution always exists.

 Sample Input

 2
 4 3
 5 5 5
 4 4 3
 6 5
 5 5 4 5 3
 1 3 2 2 1
 Sample Output

 4 4
 2 4

 * 
 * 
 * 
 * 
 */

import java.util.Scanner;

public class Main {

	public static int CASE_COUNT;
	public static int N;
	public static int M;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		CASE_COUNT = sc.nextInt();
		for (int ci = 0; ci < CASE_COUNT; ci++) {
			N = sc.nextInt() - 1;
			M = sc.nextInt();
			int sn = 0;
			int sm = 0;
			for (int i = 0; i < N; i++) {
				sn += sc.nextInt();
			}
			sn -= 1;
			for (int i = 0; i < M; i++) {
				sm += sc.nextInt();
			}
			System.out.println((sm / M + 1) + " " + sn / N);
		}
		sc.close();

	}

}
