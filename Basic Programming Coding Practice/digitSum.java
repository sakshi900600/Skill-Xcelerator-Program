
public class digitSum {
    
    public static void main(String[] args) {
        
        int n = 1234;
        int sum = 0;
        while(n > 0){
            int ld = n % 10;
            sum += ld;
            n = n/10;
        }

        System.out.println(sum);
    }

}
