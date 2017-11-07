package test;

public class Main {

	public static void main(String[] args) {

		System.out.println(normalizeName("www____c2a..de-2-"));

	}
	
	public static String normalizeName(String name){
		if(name==null){
			return "";
		}
		return name.replaceAll("_+", "_").replaceAll("[^\\.\\w]", "");
	}

}
