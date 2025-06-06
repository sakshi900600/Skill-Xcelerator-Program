import java.util.*;

public class tripletCount {



    public static long countTriplets(long[] arr, long r) {
        Map<Long, Long> leftMap = new HashMap<>();
        Map<Long, Long> rightMap = new HashMap<>();
        
        // Initialize rightMap with frequencies
        for (long num : arr) {
            rightMap.put(num, rightMap.getOrDefault(num, 0L) + 1);
        }
        
        long result = 0;
        
        for (long num : arr) {
            // Remove the current element from rightMap as it cannot be k anymore
            rightMap.put(num, rightMap.get(num) - 1);
            
            if (num % r == 0) {
                long left = num / r;
                long right = num * r;
                
                // Check if left exists in leftMap and right exists in rightMap
                result += leftMap.getOrDefault(left, 0L) * rightMap.getOrDefault(right, 0L);
            }
            
            // Add the current element to leftMap for future elements to use as i
            leftMap.put(num, leftMap.getOrDefault(num, 0L) + 1);
        }
        
        return result;
    }


    public static List<List<Integer>> findTriplets(long[] arr, long r) {
        List<List<Integer>> triplets = new ArrayList<>();
        Map<Long, List<Integer>> leftIndices = new HashMap<>();
        Map<Long, List<Integer>> rightIndices = new HashMap<>();

        // Initialize rightIndices with all elements and their indices
        for (int i = 0; i < arr.length; i++) {
            rightIndices.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }

        for (int j = 0; j < arr.length; j++) {
            long num = arr[j];
            // Remove current index from rightIndices as it cannot be k anymore
            rightIndices.get(num).remove(Integer.valueOf(j));

            if (num % r == 0) {
                long leftNum = num / r;
                long rightNum = num * r;

                if (leftIndices.containsKey(leftNum) && rightIndices.containsKey(rightNum)) {
                    List<Integer> leftList = leftIndices.get(leftNum);
                    List<Integer> rightList = rightIndices.get(rightNum);

                    for (int i : leftList) {
                        for (int k : rightList) {
                            if (i < j && j < k) {
                                triplets.add(Arrays.asList(i, j, k));
                            }
                        }
                    }
                }
            }

            // Add current index to leftIndices for future elements to use as i
            leftIndices.computeIfAbsent(num, k -> new ArrayList<>()).add(j);
        }

        return triplets;
    }


    
    public static void main(String[] args) {
        
        // int arr[] = {1,4,16,64};
        long arr[] = {1,4,16,64};
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
        System.out.println(countTriplets(arr, r));
        List<List<Integer>> ans = findTriplets(arr, r);

        for (int i = 0; i < ans.size(); i++) {
            System.out.println(ans.get(i) +" ");
        }
        

    }
}
