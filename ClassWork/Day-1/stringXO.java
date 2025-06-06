import java.util.*;

public class stringXO {

    // 1. count no of XO in string
    // 2. Count max no of XO in string
    // 3. Find out the index of max XO - start, end
    // 4. Replace the XOX with SO and then count no of SO.

    public static void main(String[] args) {

        String s = "XXXOXOXOXOOXOXOX";
        int n = s.length();

        // count no of XO -------------------------
        // int count = 0;
        // for(int i=0; i<s.length()-1; i++){
        // if(s.charAt(i)=='X' && s.charAt(i+1)=='O'){
        // count++;
        // }
        // }
        // System.out.println(count);

        // count max no of XO ---------------------------
        // int count = 0;
        // int max = 0;
        // for(int i=0; i<n-1; i++){
        // if(s.charAt(i)=='X' && s.charAt(i+1)=='O'){
        // count++;
        // i++;
        // if(max < count){
        // max = count;
        // }
        // }
        // else{
        // count = 0;
        // }
        // }
        // System.out.println(max);

        // find out the index of max XO -----------------------
        // int count = 0, max = 0;
        // int index[] = new int[2];
        // Arrays.fill(index, 0);

        // for (int i = 0; i < n - 1; i++) {
        //     if (s.charAt(i) == 'X' && s.charAt(i + 1) == 'O') {
        //         count++;
        //         if (count == 1) {
        //             index[0] = i;
        //         }
        //         i++;

        //         if (count > max) {
        //             max = count;
        //             index[1] = i + 1;
        //         }
        //     } else {
        //         count = 0;
        //     }
        // }

        // System.out.print(index[0] + " " + index[1]);

        // int count = 0;
        // int index[] = new int[2];
        // int max = 0;
        // for(int i=0; i<s.length()-1; i++){
        // if(s.charAt(i) =='X' && s.charAt(i+1)=='O'){
        // count++;
        // i++;
        // if(max < count){
        // max = count;
        // index[0] = i;
        // index[1] = i+1;
        // }
        // }
        // else{
        // count = 0;
        // }
        // }

        // System.out.println(count);
        // System.out.println(max);

        // System.out.println(index[0] + " " + index[1]);

        String replaced = s.replaceAll("XOX", "SO");

        int countSO = 0;
        for (int i = 0; i < replaced.length() - 1; i++) {
            if (replaced.charAt(i) == 'S' && replaced.charAt(i + 1) == 'O') {
                countSO++;
            }
        }

        System.out.println("Replaced String: " + replaced);
        System.out.println("Number of SO: " + countSO);

    }
}
