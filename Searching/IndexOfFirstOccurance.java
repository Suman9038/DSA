package Searching;

public class IndexOfFirstOccurance {
    // NAIVE SOLUTION
    static int firstIndex(int arr[], int x) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            if (arr[i] == x) {
                return i;
            }
        }
        return -1;
    }

    // EFFECIENT SOLUTION
    // 1.Recursive approach
    static int fOcc(int arr[], int low, int high, int x) {
        if (low > high) {
            return -1;
        }
        int mid = (low + high) / 2;
        if (x > arr[mid]) {
            return (fOcc(arr, mid + 1, high, x));
        } else if (x < arr[mid]) {
            return (fOcc(arr, low, mid - 1, x));
        } else {
            if (mid == 0 || arr[mid - 1] != arr[mid]) {
                return mid;
            } else {
                return (fOcc(arr, low, mid - 1, x));
            }
        }
    }

    // ITERATIVE WAY
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

    public static void main(String[] args) {
        int arr[] = { 10, 10, 10 };
        int x = 10;
        int n = arr.length;
        int low = 0;
        int high = n - 1;
        // System.out.println(firstIndex(arr, x));
        // System.out.println(fOcc(arr, low, high, x));
        System.out.println(firOcc(arr, n, x));
    }
}
