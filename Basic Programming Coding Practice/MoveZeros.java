import java.util.*;
public class MoveZeros {


    public static int[] moveZeros(int arr[], int n){
        int left = -1;
        for(int i=0; i<n; i++){
            if(arr[i] == 0){
                left = i;
                break;
            }
        }

        if(left == -1){
            return arr;
        }

        for (int right = left + 1; right < n; right++) {
            if (arr[right] != 0) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
            }
        }

        return arr;
    }


    public static void main(String[] args) {

        int arr[] = { 1,0,0,5,2,9,3 };
        int n = arr.length;

        
        moveZeros(arr, n);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        
        

    
        
        

        
    }
}