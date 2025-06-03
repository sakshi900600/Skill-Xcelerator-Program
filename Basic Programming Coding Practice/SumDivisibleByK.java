import java.util.*;

public class SumDivisibleByK {
    
    public static void main(String[] args) {
        
        int arr[] = {2,7,6,1,4,5};
        int k = 3;
        int n = arr.length;

        // generate all subarray
        List<List<Integer>> subarr = new ArrayList<>();
        for(int i=0; i<n; i++){
            for(int j=i; j<n; j++){
                List<Integer> list = new ArrayList<>();
                for(int x=i; x<=j; x++){
                    list.add(arr[x]);
                }
                subarr.add(list);
            }
        }

        // for(int i=0; i<subarr.size(); i++){
        //     System.out.print(subarr.get(i)+ " ");
        // }

        // traverse subarr and each time find sum & check if it is divisible by k
        int length=0, maxLength=0;
        List<List<Integer>> ans = new ArrayList<>();
        
        for(int i=0; i<subarr.size(); i++){
            int sum  = 0;
            for(int j=0; j<subarr.get(i).size(); j++){
                sum += subarr.get(i).get(j);
            }
            if(sum % k == 0){
                length = subarr.get(i).size();
                if(length > maxLength){
                    maxLength = length;
                    ans.add(subarr.get(i));
                }
            }
        }

        System.out.println(maxLength);
        System.out.println(ans.get(ans.size()-1));
        
        

    }
}
