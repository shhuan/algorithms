package open.ex.amzaon;

import java.util.Scanner;

/*
 Question:

 Given an array with positive integers and another integer for example{7 2 4} 9, you are required to generate an equation, by inserting operator add ("+") and minus ("-") among the array . The left side of equation are consist of the array and the right side of equation is the integer. here the result is 7-2+4=9



 Rules:

 Don't include any space in the generated equation.
 In case there is no way to create the equation, please output "Invalid". For example {1 1} 10, output is "Invalid"
 The length of the integer array is from 1 to 15( include 1 and 15). If the length is 1, for example the input  {7} 7, the output is 7=7
 There is no operator "+" or "-" in front of the first number: 
 Don't change the order of the numbers. For example:  {7 2 4}  9. 7-2+4=9 is correct answer, 4-2+7=9 is wrong answer.
 There could be multiple input, meaning your function could be called multiple times. Do remember print a new line after the call.  

 Sample Input and Output:

 Input:

 1 2 3 4 10

 1 2 3 4 5

 Output:

 1+2+3+4=10

 Invalid

 ---------------------------

 */
public class Equation_Easy {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNextLine()){
			String[] oprandsStr = sc.nextLine().split(" ");
			int[] oprands = new int[oprandsStr.length-1];
			int expectResult = -1;
			for(int i=0; i<oprandsStr.length; i++){
				if(i<oprands.length){
					oprands[i] = Integer.valueOf(oprandsStr[i]);
				}else{
					expectResult = Integer.valueOf(oprandsStr[i]);
				}
			}
			System.out.println(findExpress(oprands,expectResult));
		}
		sc.close();
	}
	private static String findExpress(int[] oprands, int expectResult){
		if(oprands==null || oprands.length<1){
			return "Invalid";
		}
		if(oprands.length==1){
			if(oprands[0]==expectResult){
				return oprands[0]+"="+expectResult;
			}else{
				return "Invalid";
			}
		}
		int[] operators = new int[oprands.length];
		if(findExpressImpl(oprands,operators,0,0,expectResult)){
			StringBuilder sb = new StringBuilder();
			for(int i=0; i<oprands.length;i++){
				sb.append(oprands[i]);
				if(i<oprands.length-1){
					if(operators[i+1]==1){
						sb.append("+");
					}else{
						sb.append("-");
					}
				}else{
					sb.append("=");
				}
			}
			sb.append(expectResult);
			return sb.toString();
		}
		
		return "Invalid";
	}


	/**
	 * @param oprands
	 * @param operators get the result operators, result starts from index 1, 1 represent "+", -1 represents "-"
	 * @param index initialize to 0
	 * @param result initialize to 1
	 * @param expectResult
	 * @return true if find a result
	 */
	public static boolean findExpressImpl(int[] oprands, int[] operators, int index, int result, int expectResult){
		if(result == expectResult){
			return true;
		}
		
		if(index>=oprands.length){
			return false;
		}
		
		operators[index]=1;
		if(findExpressImpl(oprands,operators,index+1,result+oprands[index],expectResult)){
			return true;
		}
		
		operators[index]=-1;
		if(findExpressImpl(oprands,operators,index+1,result-oprands[index],expectResult)){
			return true;
		}
			
		return false;
	}

}
