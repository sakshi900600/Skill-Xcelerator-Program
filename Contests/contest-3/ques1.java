import java.util.*;

public class ques1 {

    public static List<Integer> icecreamParlor(int m, List<Integer> arr) {
        List<Integer> ans = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < arr.size(); i++) {
            int cost = arr.get(i);
            int rest = m - cost;

            if (map.containsKey(rest)) {
                ans.add(map.get(rest) + 1); 
                ans.add(i + 1);
                return ans; 
            }

            map.put(cost, i);
        }

        return ans; 
    }



     public static int maximumToys(List<Integer> prices, int k){
        int maxlen = 0;
        int n = prices.size();

        Collections.sort(prices);

        for(int i=0; i<n; i++){
            for(int j=i; j<n; j++){

                int sum = 0;
                for(int x=i; x<=j; x++){
                    sum += prices.get(x);
                }

                if(sum <= k){
                    maxlen = Math.max(maxlen,(j-i+1));
                }
            }
        }

        return maxlen;
     }




    public static void main(String[] args) {
        List<Integer> li = Arrays.asList(1 ,12, 5, 111, 200, 1000 ,10);
        int m = 50;

        // List<Integer> ans = icecreamParlor(m, li);

        System.out.println(maximumToys(li, m));

        // for (Integer integer : ans) {
        //     System.out.print(integer + " ");
        // }
    }
}
