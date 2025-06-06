
public class primePrint {

    public static boolean isPrime(int num){
        if(num <=0)return false;

        for(int i=2; i*i<=num; i++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }

    
    public static void main(String[] args) {
        int n = 10;

        for(int i=2; i<=n; i++){
            if(isPrime(i)){
                System.out.print(i + " ");
            }
        }
    }
}
