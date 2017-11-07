package op.ex.common;

/**
 * @author huash06
 * 
 * 
 * 
 * 	旋转数组中的最小元素。
		题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个
		排好序的数组的一个旋转，
		输出旋转数组的最小元素。例如数组{3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数
		组的最小值为1。
		
		
		折半查找的衍生，旋转数组有一半是有序的，有一半是无序的。
		可以同样使用折半查找的方法每次确定一半的范围，通过画出图形可以容易的分析。
 *
 */
public class MinNumberInShiftArray {

	public static void main(String[] args) {
		int[] arr = new int[]{3,4,5,1,2};
		System.out.println(binarySearch(arr,1));
		System.out.println(binarySearch(arr,2));
		System.out.println(binarySearch(arr,3));
		System.out.println(binarySearch(arr,4));
		System.out.println(binarySearch(arr,5));
		System.out.println(binarySearch(arr,6));
		
	}
	
	public static int binarySearch(int[] array, int val){
		int l=0;
		int r=array.length-1;
		int mid = (l+r)/2;
		while(l<=r){
			mid=(l+r)/2;
			if(array[mid]==val){
				return mid;
			}else if(array[mid]<val){
				if(array[r]>=val){//val中间点的值大，但是比最右端的值小，所以只能在中间点和最右端之间
					l = mid+1;
				}else{
					r = mid-1;//val比中间点的值大，比最有段的值也大，说明序列旋转的节点在左边，val也在左边
				}
			}else{
				if(array[l]<=val){
					r = mid-1;
				}else{
					l = mid+1;
				}
			}
		}
		return -1;
	}

}
