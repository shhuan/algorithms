package open.ex.zoj.sim.p1138;

import java.util.Scanner;
import java.util.Stack;

/**
 * @author huash06
 *
 *
 *         题意： 求给定表达式的导数
 */
public class Main {

	public static boolean ONLINE_JUDGE = true;

	public static void main(String[] args) {
		if (!ONLINE_JUDGE) {
			System.setIn(Main.class.getClassLoader().getResourceAsStream("input_1138.txt"));
		}

		Scanner scanner = new Scanner(System.in);
		while (scanner.hasNextLine()) {
			String exp = scanner.nextLine();

			derivate(exp);
		}
		scanner.close();

	}

	private static void derivate(String exp) {
		// Expression expression = new Expression(exp, null);
		Stack<Expression> stack = new Stack<>();
		// stack.push(Expression.makeExp(exp));
		Expression expression = Expression.makeExp(exp);

	}

}

class Expression {
	public Expression expLeft;
	public Expression expRight;
	public String operator;
	public String expression;
	public String derivation;

	public Expression(Expression expLeft, Expression expRight, String operator, String expression, String derivation) {
		super();
		this.expLeft = expLeft;
		this.expRight = expRight;
		this.operator = operator;
		this.expression = expression;
		this.derivation = derivation;
	}

	public static Expression makeExp(String exp) {
		if (exp == null) {
			return null;
		}
		exp = exp.trim();
		if (exp.length() <= 0) {
			return null;
		}
		if (exp.startsWith("(")) {
			return makeExp(exp.substring(1, exp.length() - 1));
		}
		int pc = 0;
		for (int i = 0; i < exp.length(); i++) {
			char ch = exp.charAt(i);
			if (ch == '(') {
				pc++;
			} else if (ch == ')') {
				pc--;
			} else if (pc == 0) {
				if (ch == '+' || ch == '-') {
					Expression leftExp = makeExp(exp.substring(0, i));
					Expression rightExp = makeExp(exp.substring(i + 1));
					return new Expression(leftExp, rightExp, exp.substring(i, i + 1), null, null);
				}
			}
		}
		for (int i = 0; i < exp.length(); i++) {
			char ch = exp.charAt(i);
			if (ch == '(') {
				pc++;
			} else if (ch == ')') {
				pc--;
			} else if (pc == 0) {
				if (ch == '*' || ch == '/') {
					Expression leftExp = makeExp(exp.substring(0, i));
					Expression rightExp = makeExp(exp.substring(i + 1));
					return new Expression(leftExp, rightExp, exp.substring(i, i + 1), null, null);
				}
			}
		}
		if (exp.startsWith("ln")) {
			Expression rightExp = makeExp(exp.substring(2));
			return new Expression(null, rightExp, "ln", null, null);
		}
		return new Expression(null, null, null, exp, null);
	}
}
