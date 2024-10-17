public class WindowSlidingTechnique {
    //NAIVE SOLUTION (QUARDATIC SOLN)
    static int winSum(int arr[], int k) {
        int n = arr.length;
        int max_sum = Integer.MIN_VALUE;
        for (int i = 0; i <= n - k; i++) {
            int sum = 0;
            for (int j = 0; j < k; j++) {
                sum += arr[i + j];
            }
            max_sum = Math.max(sum, max_sum);
        }
        return max_sum;
    }

    //EFFECIENT SOLUTION WITH (LINEAR SOLN)
    static int winSum1(int arr[],int k,int sum)
    {
        int max_sum = Integer.MIN_VALUE;
        int n=arr.length;                  
        int currSum=0;
        for(int i =0 ; i<k ; i++) // ye loop upto k element k element tak ka value ko add karta rahega mtlb pahla consequitive ko add karega
        {
            currSum+=arr[i];
        }
        for(int i=k;i<n;i++) // ye pahle k baad wala consequitive element k a sum nikale ga 
        {
            currSum+=arr[i]-arr[i-k];
            max_sum=Math.max(max_sum, currSum);
        }
        /*VARIATION IN THIS QUESTION WHETHER THE GIVENSUM SUBARRAY IS PRESENT IN IN THE ARRAY OR NOT IF YES PRINT TRUE OR
         ELSE FALSE */

        if(sum==max_sum)
        {
           System.out.println("THE SUB ARRAY IS PRESENT");
        }
        else
        {
            System.out.println("THE SUB ARRAY IS NOT PRESENT");
        }
        return max_sum;
    }
/* ANOTHER VARIATION IN THIS IN THIS QUESTION IS IF THE ARRAY IS UNSORTED AND NON NEGATIV INTEGER THEN FIND THE SUBARRAY WITH
   GIVEN SUM IS  SO THIS PEOBLEM CANNOT BE DONE BY PREVIOUS SOLUTION WE NEED TO DIFF APPROACH 
 */
static boolean isSubSum(int arr[] , int sum)
{
    int n=arr.length;
    int currSum=arr[0];
    int start=0;
    for(int end=1; end<n;end++)
    {
        //PAHLE PREVIOUS ELEMENT AGAR H WINDOW MAI TOH DELETE KARNA HOGA 
        while (currSum>sum && start<end-1) {
            currSum-=arr[start];
            start++;
        }
        if(currSum==sum)
        {
            return true;
        }
        if(end<n)
        {
            currSum+=arr[end];
        }
    }
    return (currSum==sum);
}

    public static void main(String[] args) {
        // int arr[] = { 5, -10, 6, 90, 3 };
        // int k = 2;
        int arr[] = {1,4,20,3,10,5};
        int givenSum=33;
        // System.out.println(winSum(arr, k));
        // System.out.println(winSum1(arr, k,givenSum));
        System.out.println(isSubSum(arr,givenSum));

    }



}
