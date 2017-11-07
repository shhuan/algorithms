package op.ex.common;

/**
 * @author huash06
 *
 *
 *	题目：输入一个字符串，打印出该字符串中字符的所有排列。
	例如输入字符串abc，则输出由字符a、b、c 所能排列出来的所有字符串
	abc、acb、bac、bca、cab 和cba。
	
	
	简单递归
 */
public class AllPermOfString {

	public static void main(String[] args) {
		perm("11223".toCharArray(),0);

	}

	public static void perm(char[] charArray, int start){
		if(charArray==null || charArray.length<=0){
			return;
		}
		if(start >= charArray.length){
			System.out.println(String.valueOf(charArray));
			return;
		}
		for(int i=start; i<charArray.length; i++){
			boolean ignore = false;
			for(int j=start; j<i; j++){
				if(charArray[j]==charArray[i]){
					ignore = true;
					break;
				}
			}
			if(ignore){
				continue;
			}
			swap(charArray, start, i);
			perm(charArray, start+1);
			swap(charArray, i, start);
				
		}
	}
	public static void swap(char[] charArray, int i1, int i2){
		char tmp = charArray[i1];
		charArray[i1] = charArray[i2];
		charArray[i2] = tmp;
	}

}
