package Searching;

public class CountOccurInSortedArray {

    static int firOcc(int arr[], int n, int x) {
        int low = 0;
        int high = n - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (x > arr[mid]) {
                low = mid + 1;
            } else if (x < arr[mid]) {
                high = mid - 1;
            } else {
                if (mid == 0 || arr[mid - 1] != arr[mid]) {
                    return mid;
                } else {
                    high = mid - 1;
                }
            }
        }
        return-1;
    }

    static int lasOcc(int[] arr, int n, int x) {
        int low = 0;
        int high = n - 1;
        int result = -1; // To store the index of the last occurrence

        while (low <= high) {
            int mid = (low + high) / 2;

            if (x > arr[mid]) {
                low = mid + 1;
            } else if (x < arr[mid]) {
                high = mid - 1;
            } else {
                result = mid; 
                low = mid + 1; 
            }
        }
        return result;
    }
    static int CountOccur(int arr[],int n,int x)
    {
        int first=firOcc(arr, n, x);
        if (first==-1)
        {
            return 0;
        }
        else
        {
            return(lasOcc(arr, n, x)-first+1);
        }
    }
    public static void main(String[] args) {
        int arr[]={10,10,10,10,10,10};
        int x=10;
        int n=arr.length;
        System.out.println(CountOccur(arr, n, x));
    }
}
