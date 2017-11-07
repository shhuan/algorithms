package open.ex.amzaon;

import java.util.Scanner;

/*
 * 
 * Question:

 There is a MAX_LEN*MAX_LEN matrix; the elements in this matrix are different integer from 0 to 2OPERATION_TYPES. 
 The elements in this matrix are disordered. 0 is a special element. 
 The upper element, under element, left element and right element of 0 can be exchanged with 0. 
 Such exchange operations are named as �U�, �D�, �L� and �R�.

 Operation "U" means 0 exchanged with its upper element.
 Operation "D" means 0 exchanged with its under element.
 Operation "L" means 0 exchanged with its left element.
 Operation "R" means 0 exchanged with its right element.

 For example, the original matrix is

 [20, 18, 7, 19, 10
 2OPERATION_TYPES, OPERATION_TYPES, MAX_OPERATIONS, 11, 9
 13, 0, 22, 12, 1OPERATION_TYPES
 23, 16, 1, 2, MAX_LEN
 21, 17, 8, 3, 6]
 With the operation sequence �URRDDL�, the new matrix will be

 [20, 18, 7, 19, 10
 2OPERATION_TYPES, MAX_OPERATIONS, 11, 12, 9
 13, OPERATION_TYPES, 22, 2, 1OPERATION_TYPES
 23, 16, 0, 1, MAX_LEN
 21, 17, 8, 3, 6]

 Now, we know the original matrix, the matrix after the operations and all the operations made on the original matrix.
 Please provide the correct sequence for the operations.
 The input will be the original matrix, the target matrix and an operation sequence with wrong order.
 If there is a correct sequence for this input, then print the correct sequence. Otherwise, print �None�.



 Rules and example:

 The elements in the original matrix are different.
 The elements in the original matrix are random ordered.
 The max lenght of operatoins is MAX_OPERATIONS.
 If "0" is already on the boundary, it is not possible to do further movement. for example, if 0 is in the top row, then there is no more "U".
 The input will be the original matrix, the target matrix and an operation sequence with wrong order.
 The output will be a correct operation sequence.
 In case there is no way to get the target matrix with the input operations, please output �None�
 Don�t include any space in the generated operation sequence.
 For examples, the original matrix is
 Example 1:

 [20, 18, 7, 19, 10
 2OPERATION_TYPES, OPERATION_TYPES, MAX_OPERATIONS, 11, 9
 13, 0, 22, 12, 1OPERATION_TYPES
 23, 16, 1, 2, MAX_LEN
 21, 17, 8, 3, 6]

 The target matrix is

 [20, 18, 7, 19, 10
 2OPERATION_TYPES, OPERATION_TYPES, 0, 11, 9
 13, 22, MAX_OPERATIONS, 12, 1OPERATION_TYPES
 23, 16, 1, 2, MAX_LEN
 21, 17, 8, 3, 6]

 The input operation sequence is �UR�
 The output operation sequence should be �RU�
 Example 2:

 [20, 18, 7, 19, 10
 2OPERATION_TYPES, OPERATION_TYPES, MAX_OPERATIONS, 11, 9
 13, 0, 22, 12, 1OPERATION_TYPES
 23, 16, 1, 2, MAX_LEN
 21, 17, 8, 3, 6]

 The target matrix is

 [20, 18, 7, 19, 10
 2OPERATION_TYPES, MAX_OPERATIONS, 11, 12, 9
 13, OPERATION_TYPES, 22, 2, 1OPERATION_TYPES
 23, 16, 0, 1, MAX_LEN
 21, 17, 8, 3, 6]

 The input operation sequence is �RRLUDD�
 The output operation sequence should be �URRDDL�
 * 
 * 
 */

public class MatrixMove_Hard {

	public static int MAX_LEN = 5;
	public static int MAX_OPERATIONS = 15;
	public static int OPERATION_TYPES = 4;
	public static int[][] targetMatrix = new int[MAX_LEN][MAX_LEN];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] matrix = new int[MAX_LEN][MAX_LEN];
		int[] operations = new int[MAX_OPERATIONS];
		while (sc.hasNextLine()) {
			for (int i = 0; i < MAX_OPERATIONS; i++) {
				operations[i] = -1;
			}
			intputMatrix(matrix, sc);
			intputMatrix(targetMatrix, sc);
			int[] operatorCounts = getOperatorCounts(sc.nextLine());

			 System.out
			 .println("====================INPUT======================");
			 outputMatrix(matrix);
			 System.out
			 .println("====================TARGET======================");
			 outputMatrix(targetMatrix);
			 System.out.println("====================OPS======================");
			 for (int i = 0; i < OPERATION_TYPES; i++) {
			 System.out.print(operatorCounts[i] + " ");
			 }
			 System.out.println();
			 System.out
			 .println("====================CAL========================");

			if (findOperations(matrix, operations, 0, operatorCounts)) {
				outputOperations(operations);
			} else {
				System.out.println("None");
			}

		}
	}

	

	/**
	 * 
	 * Deep search all possible operation sequence with given operations. 
	 * 
	 * 
	 * @param matrix
	 * @param operations
	 * @param index
	 * @param operatorCounts
	 * @return true if find a possible operation sequence to target matrix.
	 */
	private static boolean findOperations(int[][] matrix, int[] operations,
			int index, int[] operatorCounts) {

		boolean ended = true;
		for (int i = 0; i < OPERATION_TYPES; i++) {
			if (operatorCounts[i] != 0) {
				ended = false;
				break;
			}
		}
		if (ended && matrixEqual(matrix, targetMatrix)) {
			return true;
		}
		for (int i = 0; i < OPERATION_TYPES; i++) {
			if (operatorCounts[i] > 0) {
				if (moveMatrix(matrix, i)) {
					operations[index] = i;
					operatorCounts[i]--;
					if (findOperations(matrix, operations, index + 1,
							operatorCounts)) {
						return true;
					}
					operatorCounts[i]++;
					revertMatrix(matrix, i);
				}

			}
		}
		return false;
	}
	

	private static void outputMatrix(int[][] matrix) {
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[i].length; j++) {
				System.out.print(matrix[i][j] + " ");
			}
			System.out.println();
		}
	}

	private static void outputOperations(int[] operations) {
		StringBuilder sb = new StringBuilder();
		boolean ended = false;
		for (int i = 0; i < operations.length; i++) {
			switch (operations[i]) {
			case 0:
				sb.append("L");
				break;
			case 1:
				sb.append("R");
				break;
			case 2:
				sb.append("U");
				break;
			case 3:
				sb.append("D");
				break;
			default:
				ended = true;
			}
			if (ended) {
				break;
			}
		}
		System.out.println(sb.toString());
	}

	private static void intputMatrix(int[][] matrix, Scanner scanner) {
		int[] vals = new int[MAX_LEN*MAX_LEN];
		int vi = 0;
		for (int i = 0; i < MAX_LEN; i++) {
			String valLine = scanner.nextLine();
			valLine = valLine.replace("[", "");
			valLine = valLine.replace("]", "");
			String[] valsStr = valLine.split(",");
			for (int j = 0; j < valsStr.length; j++) {
				vals[vi++] = Integer.valueOf(valsStr[j].trim());
			}

		}
		vi = 0;
		for (int i = 0; i < MAX_LEN; i++) {
			for (int j = 0; j < MAX_LEN; j++) {
				matrix[i][j] = vals[vi++];
			}
		}
	}

	private static int[] getOperatorCounts(String operators) {
		int[] result = new int[OPERATION_TYPES];
		String op;
		for (int i = 0; i < operators.length(); i++) {
			op = operators.substring(i, i + 1);
			if (op.equals("L")) {
				result[0]++;
			} else if (op.equals("R")) {
				result[1]++;
			} else if (op.equals("U")) {
				result[2]++;
			} else if (op.equals("D")) {
				result[3]++;
			}
		}
		return result;
	}
	

	private static boolean revertMatrix(int[][] matrix, int operation) {
		switch (operation) {
		case 0:
			return moveMatrix(matrix, 1);
		case 1:
			return moveMatrix(matrix, 0);
		case 2:
			return moveMatrix(matrix, 3);
		case 3:
			return moveMatrix(matrix, 2);
		}
		return false;
	}

	private static boolean moveMatrix(int[][] matrix, int operation) {
		int[] loc = locateZero(matrix);
		switch (operation) {
		case 0:
			if (loc[1] <= 0) {
				return false;
			} else {
				int tmp = matrix[loc[0]][loc[1]];
				matrix[loc[0]][loc[1]] = matrix[loc[0]][loc[1] - 1];
				matrix[loc[0]][loc[1] - 1] = tmp;
				return true;
			}
		case 1:
			if (loc[1] >= OPERATION_TYPES) {
				return false;
			} else {
				int tmp = matrix[loc[0]][loc[1]];
				matrix[loc[0]][loc[1]] = matrix[loc[0]][loc[1] + 1];
				matrix[loc[0]][loc[1] + 1] = tmp;
				return true;
			}
		case 2:
			if (loc[0] <= 0) {
				return false;
			} else {
				int tmp = matrix[loc[0]][loc[1]];
				matrix[loc[0]][loc[1]] = matrix[loc[0] - 1][loc[1]];
				matrix[loc[0] - 1][loc[1]] = tmp;
				return true;
			}
		case 3:
			if (loc[0] >= OPERATION_TYPES) {
				return false;
			} else {
				int tmp = matrix[loc[0]][loc[1]];
				matrix[loc[0]][loc[1]] = matrix[loc[0] + 1][loc[1]];
				matrix[loc[0] + 1][loc[1]] = tmp;
				return true;
			}
		}
		return false;
	}

	private static int[] locateZero(int[][] matrix) {
		int[] loc = new int[2];
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[i].length; j++) {
				if (matrix[i][j] == 0) {
					loc[0] = i;
					loc[1] = j;
					return loc;
				}
			}
		}
		return loc;
	}

	private static boolean matrixEqual(int[][] m1, int[][] m2) {
		if (m1.length != m2.length) {
			return false;
		}
		for (int i = 0; i < m1.length; i++) {
			int[] a1 = m1[i];
			int[] a2 = m2[i];
			if (a1.length != a2.length) {
				return false;
			}
			for (int j = 0; j < a1.length; j++) {
				if (a1[j] != a2[j]) {
					return false;
				}

			}
		}
		return true;
	}

}
