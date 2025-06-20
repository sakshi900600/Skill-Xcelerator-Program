import java.util.*;
public class trydl{


    public static int[] intersecArr(int nums1[], int nums2[]){
        Set<Integer> set = new HashSet<>();
        int n = nums1.length;
    
        for(int i=0; i<n; i++){
            if(nums1[i] == nums2[i]){
                set.add(nums1[i]);
            }
        }

        int ans[] = new int[set.size()];
        int i=0;
        for(int elem: set){
            ans[i] = elem;
            i++;
        }

        return ans;
    }



    public static void main(String args[]){

        int arr1[] = {4,9,5};
        int arr2[] = {9,4,9,8,4};

        
        int ans[] = intersecArr(arr1, arr2);

        for(int i=0; i<ans.length; i++){
            System.out.print(ans[i]);
        }


    }
}