public class subarrProduct {
    


    public static void main(String[] args) {
        

        int arr[] = {10,5,2,6};
        int target=100;
        int n = arr.length;

        int count = 0;
        for(int i=0; i<n; i++){
            
            for(int j=i; j<n; j++){
                int product = 1;
                for(int k=i; k<=j; k++){
                    product *= arr[k];
                }

                if(product < target){
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}
