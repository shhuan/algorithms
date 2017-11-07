package op.ex.common;

public class BigNumber {

	public static void main(String[] args) {
		System.out.println("===========ADD=============");
		System.out.println(ADD_INT("21234", "-89321"));
		System.out.println(ADD_INT("1234", "-89321"));
		System.out.println(ADD_INT("21234", "-8931"));
		System.out.println(ADD_INT("9213","789"));
		System.out.println(ADD_INT("-21234", "-89321"));
		System.out.println(ADD_INT("-21234", "89321"));
		System.out.println(ADD_INT("000321312", "003789809"));
		
		System.out.println("===========MINUS=============");
		System.out.println(MINUS_INT("213", "899"));
		System.out.println(MINUS_INT("213", "899"));
		System.out.println(MINUS_INT("-213", "899"));
		System.out.println(MINUS_INT("213", "-899"));
		
		System.out.println("===========MUL=============");
		System.out.println(MUL_INT("213", "899"));
		System.out.println(MUL_INT("-213", "899"));
		System.out.println(MUL_INT("213", "-899"));
		System.out.println(MUL_INT("-213", "-899"));
		System.out.println(MUL_INT("867", "27"));
		System.out.println(MUL_INT("867", "0"));
		System.out.println(MUL_INT("00867", "1"));
		System.out.println(MUL_INT("00867", "-0"));

		
		System.out.println("===========DIV=============");
		System.out.println(DIV_INT("213", "1"));
		System.out.println(DIV_INT("-213", "0"));
		System.out.println(DIV_INT("213", "-899"));
		System.out.println(DIV_INT("867", "27"));
		System.out.println(DIV_INT("00867", "022"));
		
		System.out.println("===========FLOAT ADD=============");
		System.out.println(FLOAT_ADD("21.2323", "1.987"));
		System.out.println(FLOAT_ADD("213", "-899"));
		
	}
	
	/**
	 * 
	 * 浮点数的高精度操作都可以转换为整数的操作，然后加上小数点
	 * 
	 * @param numA	加数
	 * @param numB	被加数
	 * @return	和
	 */
	public static String FLOAT_ADD(String numA, String numB){
		int diA = numA.indexOf('.');
		diA = diA>0?numA.length()-diA-1:0;//numA的小数部分的位数		
		int diB = numB.indexOf('.');
		diB = diB>0?numB.length()-diB-1:0;//numB的小数部分的位数
		int di = diA>diB?diA:diB;
		if(di>0){
			StringBuilder sb = new StringBuilder();
			for(int i=0; i<di-diA; i++){
				sb.append('0');
			}
			if(sb.length()>0){
				numA = numA+sb.toString();
				sb = new StringBuilder();
			}
			for(int i=0; i<di-diB; i++){
				sb.append('0');
			}
			if(sb.length()>0){
				numB = numB+sb.toString();
			}
			String sum = ADD_INT(numA.replace(".", ""), numB.replace(".", ""));
			int spi = sum.length()-di;
			return sum.substring(0,spi)+"."+sum.substring(spi);
		}else{
			return ADD_INT(numA, numB);
		}
	}

	public static String ADD_INT(String numA, String numB){
		if(numA.startsWith("-")){
			if(numB.startsWith("-")){
				return "-"+ADD_INT(numA.substring(1), numB.substring(1));
			}else{
				return MINUS_INT(numB, numA);
			}
		}else{
			if(numB.startsWith("-")){
				return MINUS_INT(numA, numB.substring(1));
			}else{
				numA = removePreviousZero(numA);
				numB = removePreviousZero(numB);
				int len = numA.length()>numB.length()?numA.length():numB.length();
				StringBuilder sb = new StringBuilder();
				for(int i=0; i<len-numA.length(); i++){
					sb.append("0");
				}
				if(sb.length()>0){
					numA = sb.toString()+numA;
					sb = new StringBuilder();
				}
				for(int i=0; i<len-numB.length(); i++){
					sb.append("0");
				}
				if(sb.length()>0){
					numB = sb.toString()+numB;
				}
				
				
				char[] charA = numA.toCharArray();
				char[] charB = numB.toCharArray();
				char[] sum = new char[len+1];
				int val=0;
				int cap=0;
				for(int i=len-1; i>=0; i--){
					val = (charA[i]-'0')+(charB[i]-'0')+cap;
					cap = val/10;
					val %= 10;
					sum[i+1] = (char) (val+'0');
				}
				sum[0] = (char) (cap+'0');
				return removePreviousZero(String.valueOf(sum));
			}
		}
	}
	public static String MINUS_INT(String numA, String numB){
		if(numA.startsWith("-")){
			if(numB.startsWith("-")){
				return MINUS_INT(numB.substring(1),numA.substring(1));
			}else{
				return MINUS_INT(numB.substring(1),numA);
			}
		}else{
			if(numB.startsWith("-")){
				return ADD_INT(numA, numB.substring(1));
			}else{
				numA = removePreviousZero(numA);
				numB = removePreviousZero(numB);
				if(compare(numA, numB)<0){
					return "-"+MINUS_INT(numB, numA);
				}
				if(numA.length()<numB.length()){
					return "-"+MINUS_INT(numB, numA);
				}else{
					StringBuilder sb = new StringBuilder();
					for(int i=0; i<numA.length()-numB.length();i++){
						sb.append("0");
					}
					numB = sb.toString()+numB;
					char[] charA = numA.toCharArray();
					char[] charB = numB.toCharArray();
					char[] diff =new char[numA.length()];
					int cap = 0;
					int val = 0;
					for(int i=numA.length()-1; i>=0; i--){
						val = charA[i] - charB[i] -cap;
						if(val<0){
							cap = 1;
							val += 10;
						}else{
							cap = 0;
						}
						diff[i] = (char) (val+'0');
					}
					return removePreviousZero(String.valueOf(diff));
				}
			}
		}
	}
	public static String MUL_INT(String numA, String numB){
		if(numA.startsWith("-")){
			if(numB.startsWith("-")){
				return MUL_INT(numA.substring(1),numB.substring(1));
			}else{
				return "-"+MUL_INT(numA.substring(1),numB);
			}
		}else{
			if(numB.startsWith("-")){
				return "-"+MUL_INT(numA, numB.substring(1));
			}else{
				if(compare(numA, numB)<0){
					return MUL_INT(numB, numA);
				}else{
					char[] mul = new char[numA.length()+numB.length()+1];//结果最多是两个数的位数的和+1
					for(int i=0; i<mul.length; i++){
						mul[i] = '0';
					}
					for(int i=numB.length()-1; i>=0; i--){//模拟手工乘法
						int cap = 0;
						int val = 0;
						int mi = numA.length()+1+i;
						for(int j=numA.length()-1; j>=0; j--){
							int tmul = (numB.charAt(i)-'0')*(numA.charAt(j)-'0') + cap;
							tmul += mul[mi]-'0';
							cap = tmul/10;
							val = tmul%10;
							mul[mi] = (char) (val+'0');
							mi--;
						}
						while(cap>0){
							val = (mul[mi]-'0')+cap;
							cap = val/10;
							val %= 10;
							mul[mi] = (char) (val+'0');
							mi--;
						}
					
					}
					return removePreviousZero(String.valueOf(mul));
				}
			}
		}
	}
	public static String DIV_INT(String numA, String numB){
		numA = removePreviousZero(numA);
		numB = removePreviousZero(numB);
				
		if(numA.startsWith("-")){
			if(numB.startsWith("-")){
				return DIV_INT(numA.substring(1), numB.substring(1));
			}else{
				return DIV_INT(numA.substring(1), numB);
			}
		}else{
			if(numB.startsWith("-")){
				return "-"+DIV_INT(numA, numB.substring(1));
			}
		}
		
		if(numB.equalsIgnoreCase("0")){
			return "NAN";
		}
		if(compare(numA, numB)<0){
			return "0";
		}
		if(numA.length() == numB.length()
				|| (numA.length() == numB.length()+1 && compare(MUL_INT(numB, "10"), numA)>0)){
			for(int i=9; i>0; i--){
				if(compare(MUL_INT(numB, String.valueOf(i)), numA)<=0){
					return String.valueOf(i);
				}
			}
		}

		char[] div = new char[numA.length()];
		String rem = numA;//余数
		int di = 0;
		while(compare(rem, numB)>=0){//模拟手工除法
			for(int i=numB.length(); i<=rem.length(); i++){
				String divisor = rem.substring(0,i);
				String tmpRem = "";
				if(compare(divisor, numB)>0){
					int tmpDiv = Integer.valueOf(DIV_INT(divisor, numB));
					div[di++] = (char) (tmpDiv+'0');
					tmpRem = MINUS_INT(divisor, MUL_INT(numB, String.valueOf(tmpDiv)));
					rem = tmpRem + rem.substring(i);
					break;
				}
			}
		}
		for(int i=0; i<numA.length(); i++){
			if(!(div[i]>='0' && div[i]<='9')){
				return String.valueOf(div).substring(0,i);
			}
		}
		return String.valueOf(div);
	}
	public static int compare(String numA, String numB){
		if(numA.startsWith("-")){
			if(numB.startsWith("-")){
				return compare(numB.substring(1), numA.substring(1));
			}else{
				return -1;
			}
		}else{
			if(numB.startsWith("-")){
				return 1;
			}else{
				if(numA.length()>numB.length()){
					return 1;
				}else if(numA.length()<numB.length()){
					return -1;
				}else{
					for(int i=0; i<numB.length(); i++){
						if(numA.charAt(i)>numB.charAt(i)){
							return 1;
						}else if(numA.charAt(i)<numB.charAt(i)){
							return -1;
						}
					}
					return 0;
				}
			}
		}
	}
	public static String removePreviousZero(String num){
		if(num.startsWith("-")){
			for(int i=1; i<num.length(); i++){
				if(num.charAt(i)!='0'){
					return "-"+num.substring(i);
				}
			}
		}else{
			for(int i=0; i<num.length(); i++){
				if(num.charAt(i)!='0'){
					return num.substring(i);
				}
			}
		}
		return "0";
	}

}
