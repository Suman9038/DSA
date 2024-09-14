public class Maximum_Lenght_Even_Odd_Subarray {
    // NAIVE SOLUTION 

    static void getevenodd(int arr[])
    {
        int n=arr.length;
        int res=1;
        for(int i=0;i<n;i++)
        {
            int curr_len=1;
            for(int j=i+1;j<n;j++)
            {
                if((arr[j] % 2 ==0 && arr[j-1] % 2 !=0 || arr[j] % 2 !=0 && arr[j-1] % 2 ==0  ))
                {
                    curr_len++;
                    res=Math.max(curr_len, res);
                }
                else{

                    break;
                }
            }
        }
        System.out.println(res);
    }

    // EFFECIENT SOLUTION 

    static void getEvenOdd(int arr[])
    {
        int n=arr.length;
        int res=1;
        int curr_len=1;
        for(int i=1;i<n;i++) // left se right traverse hoga 
        {
            if((arr[i] % 2 ==0 && arr[i-1] % 2 !=0 || arr[i] % 2 !=0 && arr[i-1] % 2 ==0  )) 
            {
                curr_len++;                       // chahe ye current sub array ko extend karega
                res=Math.max(curr_len, res);
            }
            else{
                                                // ya fir wo previous sub array ko extend karega
                curr_len=1;
            }
        }
        System.out.println(res);
    }
    public static void main(String[] args) {
        int arr[] = {5,10,20,6,3,8};
        // getevenodd(arr);
        getEvenOdd(arr);
    }
    
}
