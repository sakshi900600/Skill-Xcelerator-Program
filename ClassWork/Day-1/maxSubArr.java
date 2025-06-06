public class maxSubArr{



    public static void main(String[] args) {
        
        // maximum subarray sum

        int arr[] = {2,-1,-5,6,-1,3,10};
        int n = arr.length;
        
        int maxGlobal = -100;
        for(int len=1; len<=n; len++){
            int maxLocal = -100;
            int sumLocal = 0;
            for(int i=0; i<len; i++){
                sumLocal += arr[i];
            }

            if(maxLocal < sumLocal){
                maxLocal = sumLocal;
            }

            for(int i=len; i<n; i++){
                sumLocal += arr[i] - arr[i-len];
                if(maxLocal < sumLocal){
                    maxLocal = sumLocal;
                }                
            }

            if(maxGlobal < maxLocal){
                maxGlobal = maxLocal;
            }
        }

        // System.out.println(maxGlobal);





        

        




    }
}