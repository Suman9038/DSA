package Searching;

public class IndexOfLastoccurance {
    // NAIVE SOLUTION
    static int lastIndex(int arr[], int x) {
        int n = arr.length;
        for (int i = n - 1; i >= 0; i--) {
            if (arr[i] == x) {
                return i;
            }
        }
        return -1;
    }

    // EFFECIENT SOLUTION
    // 1.Recursive approach
    static int lOcc(int arr[], int low, int high, int x, int n) {
        if (low > high) {
            return -1;
        }
        int mid = (low + high) / 2;
        if (x > arr[mid]) {
            return (lOcc(arr, mid + 1, high, x, n));
        } else if (x < arr[mid]) {
            return (lOcc(arr, low, mid - 1, x, n));
        } else {
            if (mid == n - 1 || arr[mid] != arr[mid + 1]) {
                return mid;
            } else {
                return (lOcc(arr, mid + 1, high, x, n));
            }
        }
    }

    // ITERATIVE WAY
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

    public static void main(String[] args) {
        int arr[] = { 5, 10, 10, 10, 10, 20, 20 };
        int x = 10;
        int n = arr.length;
        int low = 0;
        int high = n - 1;
        // System.out.println(lastIndex(arr, x));
        // System.out.println(lOcc(arr, low, high, x,n));
        System.out.println(lasOcc(arr, n, x));
    }
}
