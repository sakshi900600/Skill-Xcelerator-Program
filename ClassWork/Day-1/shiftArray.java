public class shiftArray {
    
    // ques: shift/rotate arr elem by k

    // logic 1: 
    // create a new array and find out the new indexes of the old arr elem in newarray
    // then put old array elem at the new index in new Array & done
    // for left shift: (i+k)%n
    // for right shift: (i-k+n)%n



    // logic-2: 
    // first reverse the k elements
    // then reverse remaining n-k elem
    // then again reverse the whole array. 

    // after first k reversal(1,2)   after n-k reversal (10,11,9,8)
    // reversing whole array: (8,9,11,10,2,1) - ans. 
    


    public static void main(String[] args) {
        
        int arr[] = {2,1,8,9,10,11};

        
        int k = 2;
        int n = arr.length;
        int newArr[] = new int[n];
        // for left shift: (i+k)%n
        // for right shift: (i-k+n)%n

        for(int i=0; i<n; i++){
            int inew = (i-k+n) % n;
            newArr[inew] = arr[i];
        }

        for (int i = 0; i < newArr.length; i++) {
            System.out.print(newArr[i] + " ");
        }
    }
}
