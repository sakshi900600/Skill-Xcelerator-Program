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

    public static void main(String[] args) {

        String s = "0011";
        int n = s.length();

        int count = 0;

        // generate all substring

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                System.out.print(s.substring(i, j)+ " ");
                String subStr = s.substring(i, j);
                if (count0(subStr) == count1(subStr)) {
                    count++;
                }
            }
        }

        System.out.println("count "+ count);
    }
}
