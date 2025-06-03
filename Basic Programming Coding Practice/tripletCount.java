import java.util.*;

public class tripletCount {
    
    public static void main(String[] args) {
        
        int arr[] = {1,4,16,64};
        int r = 4;
        int n = arr.length;

        // Approach 1

        // int count = 0;
        // List<List<Integer>> list = new ArrayList<>();
        // for(int i=0; i<n; i++){
        //     for(int j=i+1; j<n; j++){
        //         for(int k=j+1; k<n; k++){
        //             if(arr[j] == arr[i]*r && arr[k] == arr[j]*r){
        //                 list.add(Arrays.asList(arr[i], arr[j], arr[k]));
        //                 count++;
        //             }
        //         }
        //     }
        // }

        // System.out.println(count);
        // for (int i = 0; i < list.size(); i++) {
        //     System.out.print(list.get(i) + " ");
        // }
        // System.out.println();



        // trying to optimize ...........................
        int left=0, right=n-1;
        int count = 0;
        for(int i=left+1; i<n; i++){
            while(left < right){
                if(arr[i] == arr[left]*r && arr[right]== arr[i]*r){
                    count++;
                }
                else if(arr[right] < arr[i]*r ){
                    right--;
                }
                else{
                    left++;
                }
            }
        }

        System.out.println(count);


    }
}
