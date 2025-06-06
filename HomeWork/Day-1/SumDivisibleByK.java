import java.util.*;

public class SumDivisibleByK {


    public static void subarrSumdbk(int arr[], int k, int n){
        // Create a hash map to store the first occurrence of each modulo result
        HashMap<Integer, Integer> modMap = new HashMap<>();
        modMap.put(0, -1); // Base case for prefix sum starting from index 0

        int prefixSum = 0;
        int maxLength = 0;
        int startIndex = -1;
        int endIndex = -1;

        for (int i = 0; i < n; i++) {
            prefixSum += arr[i];
            int mod = (prefixSum % k + k) % k; // Handle negative numbers

            if (modMap.containsKey(mod)) {
                int prevIndex = modMap.get(mod);
                if (i - prevIndex > maxLength) {
                    maxLength = i - prevIndex;
                    startIndex = prevIndex + 1;
                    endIndex = i;
                }
            } else {
                modMap.put(mod, i);
            }
        }

        if (maxLength > 0) {
            System.out.println("Maximum length of subarray with sum divisible by " + k + ": " + maxLength);
            System.out.print("Subarray: [");
            for (int i = startIndex; i <= endIndex; i++) {
                System.out.print(arr[i]);
                if (i < endIndex) {
                    System.out.print(", ");
                }
            }
            System.out.println("]");
        } else {
            System.out.println("No subarray found with sum divisible by " + k);
        }
    
    }

    
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
        subarrSumdbk(arr, k, n);






        
        
        

    }
}
