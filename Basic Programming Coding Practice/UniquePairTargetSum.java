import java.util.*;
public class UniquePairTargetSum {


    

    
    public static void main(String[] args) {
        
        int arr[] = {1,2,3,4,5,6,7};
        int target = 8;
        int n = arr.length;
        int left=0, right=n-1;

        List<List<Integer>> list = new ArrayList<>();
        while(left < right){
            int sum = arr[left] + arr[right];
            if(sum == target){
                list.add(Arrays.asList(arr[left], arr[right]));
                left++;
                right--;
            }
            else if(sum < target){
                left++;
            }
            else{
                right--;
            }
        }

        for(int i=0; i<list.size(); i++){
            System.out.print(list.get(i)+ " ");
        }

    }
}
