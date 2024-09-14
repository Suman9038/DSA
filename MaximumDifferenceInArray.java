public class MaximumDifferenceInArray {
    //NAIVE SOLN-0(n)
    static  void maxdiff(int arr[],int n )
    {
        int res=arr[1]-arr[0];
        for(int i=0;i<n-1;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if (arr[j] - arr[i] > res)
                {
                    res=arr[j]-arr[i];
                }
            }
        }
        System.out.println(res);
    }
    //EFFECIENT SOLUTION

    static void maxdifference(int arr[],int n)
    {
        int res=arr[1]-arr[0];
        int min_val=arr[0];
        for(int i=1;i<n;i++)
        {
            if(arr[i]-min_val>res)
            {
                res=arr[i]-min_val;
            }
            if(arr[i]<min_val)
            {
                min_val=arr[i];
            }
        }
        System.out.println(res);
    }
    public static void main(String[] args) {
        int arr[]={2,3,10,6,4,8,1};
        int n=arr.length;
        //maxdiff(arr, n);
        maxdifference(arr, n);

    }
    
}
