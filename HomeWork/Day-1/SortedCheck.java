public class SortedCheck {
    
    

    public static void main(String[] args) {
        
        int arr[] = {1,2,2,4};
        int n = arr.length;
        boolean isSorted = true;
        for(int i=0; i<n-1; i++){
            if(arr[i] > arr[i+1]){
                isSorted = false;
                break;
            }
        }

        System.out.println(isSorted);
    }
}
