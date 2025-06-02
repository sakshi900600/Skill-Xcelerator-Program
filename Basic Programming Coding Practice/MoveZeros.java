public class MoveZeros {

    public static void main(String[] args) {

        int arr[] = { 0, 1, 0, 3, 12 };
        int n = arr.length;
        int left = 0;
        for (int right = left + 1; right < n; right++) {
            if (arr[right] != 0) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}