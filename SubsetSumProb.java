public class SubsetSumProb {
   static int CountSubset(int arr[],int n,int sum)
    {
        if(sum ==0)
        return 1;

        if(n==0)
        return 0;

       return CountSubset(arr, n-1, sum) + CountSubset(arr, n-1, sum-arr[n-1]);

        }
    public static void main(String[] args) {
        int arr[] = { 10, 20, 15 };
        int sum = 9;
        int n = arr.length;
        if (CountSubset(arr, n, sum) == 1)
            System.out.println("Found a subset"
                            + " with given sum");
        else
            System.out.println("No subset with"
                            + " given sum");
    }
    
}
