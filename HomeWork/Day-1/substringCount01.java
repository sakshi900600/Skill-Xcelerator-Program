import java.util.*;

public class substringCount01 {

    public static int count0(String s) {
        int count = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (ch == '0') {
                count++;
            }
        }
        return count;
    }

    public static int count1(String s) {
        int count = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (ch == '1') {
                count++;
            }
        }
        return count;
    }



    // why this?  -  coz ques ask to count consecutive 0 & 1 and here we are doing same &  adding min of 0 & 1 count as final count. 

    // Why minimum? - suppose string is 00011 then here count0=3, count1=2  but the final substring which will have equal no of 0 & 1 will be: 0011 & 01  == 2
    // And the same goes for all substrings.  So it works. 
    
    public static int countSubstring(String s, int n){
        int count = 0;
        int i=0;

        while(i<n){
            int count0=0, count1=0;

            if(s.charAt(i) == '0'){
                while(i<n && s.charAt(i) == '0'){
                    count0++;
                    i++;
                }

                int j=i;
                while(j<n && s.charAt(j) == '1'){
                    count1++;
                    j++;
                }

            }
            else{
                while(i<n && s.charAt(i)=='1'){
                    count1++;
                    i++;
                }
                int j=i;
                while(j<n && s.charAt(j)=='0'){
                    count0++;
                    j++;
                }

            }

            count += Math.min(count0, count1);
        }

        return count;
    }



    public static void main(String[] args) {

        String s = "00110011";
        int n = s.length();

        
        // System.out.println(s.substring(0, n));
        
        // generate all substring
        // int count = 0;
        // for (int i = 0; i < n; i++) {
        //     for (int j = i + 1; j <= n; j++) {
        //         System.out.print(s.substring(i, j)+ " ");
        //         String subStr = s.substring(i, j);
        //         if (count0(subStr) == count1(subStr)) {
        //             count++;
        //         }
        //     }
        // }

        // System.out.println("count "+ count);


        // the above code will find out all teh substrings and count will also include 0101 although it has same no of 0 & 1 but here we need substring in which first come same no of 0 and then same no of 1 or vice versa. 


        // "0011", "01", "1100", "10", "0011","01"

        System.out.println(countSubstring(s, n));










    }
}
