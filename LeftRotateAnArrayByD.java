public class LeftRotateAnArrayByD {

    // METHOD -1(NAIVE SOLUTION)
    static void leftRotatebyOne(int arr[], int n) {
        int temp = arr[0];
        for (int i = 1; i < n; i++) {
            arr[i = 1] = arr[i];
        }
        arr[n - 1] = temp;

    }

    static void leftRotate(int arr[], int n, int d) {
        for (int i = 0; i < d; i++) {
            leftRotatebyOne(arr, n);

        }

    }
    //METHOD-2(BETTER SOOLUTION)
    static void leftRotate1(int arr[],int n,int d)
    {
        int temp[]=new int[d];
        for(int i=0;i<d;i++)
        {
            temp[i]=arr[i];
        }
        for(int i=d;i<n;i++)
        {
            arr[i-1]=arr[i];

        }
        for(int i=0;i<d;i++)
        {
            arr[n-d+i]=temp[i];
        }
        for(int j=0;j<n;j++)
        {
            System.out.println(arr[j]);
        }

    }
    //METHOD-3
    static void leftRotate2(int arr[],int n,int d)
    {
        reverse(arr,0,d-1);
        reverse(arr,d,n-1);
        reverse(arr,0,n-1);
        for(int j=0;j<n;j++)
        {
            System.out.println(arr[j]);
        }
    }
    static void reverse(int arr[],int low,int high)
    {
        while(low<high)
        {
            int temp=arr[low];
            arr[low]=arr[high];
            arr[high]=temp;
            low++;
            high--;
        }
    }
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5 };
        int n = arr.length;
        //leftRotate(arr, n, 2);
        //leftRotate1(arr, n, 2);
        leftRotate2(arr, n, 2);
    }

}
