public class PrefixSum {
    /*
     * 1. Given a fixed array and multiple quireies of following types on array, how
       to effeciently perform the quries
     */

    // NAIVE SOLUTION
    static int Sum(int arr[], int left, int right) {
        int sum = 0;
        for (int i = left; i <= right; i++) {
            sum += arr[i];
        }
        return sum;
    }
    // EFFECIENT SOLUTION 
    static int pre_sum[];
    static void getSum(int arr[],int left,int right)
    {
        int sum=0;
        if(left!=0)
        {
             System.out.println(pre_sum[right] - pre_sum[left-1]);
        }
        else
        {
            System.out.println(pre_sum[right]);
        }
    }

    /*
     * Given an arrray of an integer , find if it has an equilibrium point or not 
     */

    //NAIVE SOLUTION

    static boolean eqSum(int arr[])
    {
        int n=arr.length;
        for(int  i =0;i<n;i++)
        {
            int lSum=0,rSum=0;
            for(int j=0;j<i;j++)
            {
                lSum+=arr[j];
            }
            for(int k=i+1;k<n;k++)
            {
                rSum+=arr[k];
            }
            if(lSum==rSum)
            {
                return true;
            }
        }
        return false;
      
    }

    // EFFECIENT SOLUTOION
    static boolean equiliSum(int arr[])
    {
        int lsum=0;
        int n= arr.length;
        int sum=0;
        for(int i =0;i<n;i++)
        {
            sum+=arr[i];
        }
        for(int i =0;i<n;i++)
        {
            if(lsum == sum-arr[i])
            {
                return true;
               
            }
            lsum+=arr[i];
            sum-=arr[i];
        }
        return false;
    }
    public static void main(String[] args) {
        // int arr[]={2,8,3,9,6,5,4};
        int arr[]={3,4,8,-9,20,6};
        
        int n=arr.length;
        pre_sum = new int[n];
        pre_sum[0]=arr[0];
        for(int i=1;i<n;i++)
        {
            pre_sum[i]=pre_sum[i-1]+arr[i];
        }
        // getSum(arr, 0, 2);
       System.out.println(eqSum(arr)); 
       System.out.println(equiliSum(arr));
        // System.out.println(Sum(arr, 0, 2));
        // System.out.println(Sum(arr, 1, 3));
        // System.out.println(Sum(arr, 2, 6));
    }
}
