public class MaximumSumSubArray {
    // NAIVE SOLUTION

    static void maxsum(int arr[])
    {
        int res=arr[0];
        int n=arr.length;
        for(int i=0;i<n;i++)
        {
            int curr=0;
            for(int j=i;j<n;j++)
            {
                curr=curr=arr[j];
                res=Math.max(curr, res);
            }
        }
        System.out.println(res);
    }

    // EFFECIENT SLUTION
    static void maxSum(int arr[])
    {
        int res=arr[0];
        int n=arr.length;
        int maxEnding=arr[0]; // Because pahle element k left mai kuch nahi h toh uska max ending wahi hoga
        for(int i=1;i<n;i++)
        {
            maxEnding=Math.max(maxEnding + arr[i], arr[i]);
            res=Math.max(maxEnding, res);
        }
        System.out.println(res);
    }
    public static void main(String[] args) {
        // int arr[]={1,-2,3,-1,2};\
        int arr[]={-3,8,-2,4,-5,6};
        //maxsum(arr);
        maxSum(arr);
    }
    
}
