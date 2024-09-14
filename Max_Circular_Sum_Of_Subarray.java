public class Max_Circular_Sum_Of_Subarray {
    // Naive Solution 
    static void cicularMax(int arr[])
    {
        int n = arr.length;
        int res=arr[0];
        for(int i=0;i<n;i++) // Traverse in an array to find the 
        {
            int curr_max=arr[i];// Max always first elment rahega q ki concept hi wahi ki sare element uske beginig treat kiya jayega
            int curr_sum=arr[i];
            for(int j = 1 ; j < n ; j++) // sub array nikalne k liye ye 
            {
                int index= (i+j)%n;
                curr_sum += arr[index];
                curr_max= Math.max(curr_sum,curr_max);
            }
            res=Math.max(curr_max, res);
        }
        System.out.println(res);
    }
    // Efficient Solution 

    static int NormalmaxSum(int arr[])
    {
        int res=arr[0];
        int n=arr.length;
        int maxEnding=arr[0]; // Because pahle element k left mai kuch nahi h toh uska max ending wahi hoga
        for(int i=1;i<n;i++)
        {
            maxEnding=Math.max(maxEnding + arr[i], arr[i]);
            res=Math.max(maxEnding, res);
        }
        return res;
    }

    static void getCircularSum(int arr[])
    {
        int res=arr[0];
        int n= arr.length;
        int Max_Normal=NormalmaxSum(arr); // Max sub of normal subarray
        if(Max_Normal < 0) // check if all the element in the array is negative or not
        {
            System.out.println(Max_Normal);
        }
        int arr_Sum=0;
        for(int i = 0; i < n;i++)
        {
            arr_Sum += arr[i]; // sub of all the element in the arrray
            arr[i] = -arr[i]; // inverting all the element if the array to get the minimum sum value of normal sub array 
        }
        int max_CircularSum=arr_Sum + NormalmaxSum(arr); // taking out the cirular
        res= Math.max(Max_Normal, max_CircularSum); // getting the maximum result 
        System.out.println(res);
    }
    public static void main(String[] args) {
        int arr[]={-5,-3 };
        //cicularMax(arr);
        getCircularSum(arr);

    }
    
}
