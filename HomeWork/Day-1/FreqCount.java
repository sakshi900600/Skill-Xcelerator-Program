import java.util.*;
public class FreqCount {
    

    public static void main(String[] args) {
        
        String s = "apple";
        int n = s.length();
        Map<Character, Integer> map = new HashMap<>();

        for(int i=0; i<n; i++){
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0)+1);
        }

        // if want in sorted order then use TreeMap.
        Map<Character, Integer> sortedMap = new TreeMap<>(map);

        for(Map.Entry<Character, Integer> entry: sortedMap.entrySet()){
            System.out.print(entry.getKey() + ":" + entry.getValue()+" ");
        }
        System.out.println();
    }
}
