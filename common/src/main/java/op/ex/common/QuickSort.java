package op.ex.common;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.IntStream;

/**
 * Created by huash on 2015/7/28.
 */
public class QuickSort {

    public static void quickSort(int[] input, int left, int right){
        if(input == null  || left >= right){
            return;
        }
        int pivot = partition(input, left, right);
        quickSort(input, left, pivot-1);
        quickSort(input, pivot + 1, right);

    }
    public static int partition(int[] input, int left, int right){
        if(left > right){
            return -1;
        }else if(left == right){
            return left;
        }

        {
            //随机化
            int i = new Random().nextInt(right-left+1)+left;
            swap(input, i, right);

        }
        int pivot = input[right];

        //注意这里，如果赋值为i=left，后面就不好处理++
        int i = left-1;
        for(int j=left; j<right; j++){
            if (input[j] <= pivot){
                i++;
                swap(input, i, j);
            }
        }
        i++;
        swap(input, i, right);
        return i;
    }
    public static void swap(int[] input, int i, int j){
        int tmp = input[i];
        input[i] = input[j];
        input[j] = tmp;
    }

    public static void printList(int[] input){
        if (input == null || input.length <= 0){
            System.out.println("[]");
        }
        IntStream.range(0, input.length).forEach(i->
                System.out.print(input[i]+", ")
        );
        System.out.println();
    }
    public static void main(String[] args){

        Random rand = new Random();
        for (int i = 0; i < 10; i++) {
            int len = rand.nextInt(10);
            int[] input = new int[len];
            for (int j = 0; j < len; j++) {
                input[j] = rand.nextInt(100);
            }
            printList(input);
            quickSort(input, 0, input.length-1);
            printList(input);
            System.out.println();
        }

    }
}
