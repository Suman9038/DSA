public class ReverseAnArray {
    static void reverse(int arr[],int n)
    {
        int low=0;
        int high=n-1;
        while(low<high)
        {
            int temp=arr[low];
            arr[low]=arr[high];
            arr[high]=temp;
            low++;
            high--;
        } 
        for(int i=0;i<n;i++)
        {
            System.out.println(arr[i]);
        }
    }
    public static void main(String[] args) {
        int arr[]={30,7,6,5,10};
        int n=arr.length;
        reverse(arr, n);
    }
    
}
