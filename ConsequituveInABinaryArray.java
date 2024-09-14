public class ConsequituveInABinaryArray {
    //NAIVE SOLUTION
    static void getConsequitive(int arr[])
    {
        int n=arr.length;
        int res=0;
        int curr=0;
        for(int i=0;i<n;i++)
        {
            curr=0;
            for(int j=0;j<n;j++)
            {
                if (arr[j] == 1)
                {
                    curr++;
                    res=Math.max(curr, res);
                }
                else{

                    curr=0;
                }
                
            }
        }
        System.out.println(res);
    }

    // EEFECIENT SOLN
    static void geCons(int arr[])
    {
        int n=arr.length;
        int res=0;
        int curr=0;
        for(int i=0;i<n;i++)
        {
            if(arr[i]==0)
            {
                curr=0;
            }
            else
            {
                curr++;
                res=Math.max((curr),res);
            }
        }
        System.out.println(res);
    }
    public static void main(String[] args) {
        int arr[]={0,1,1,0,1,1,1};
        getConsequitive(arr);
        geCons(arr);
    }
    
}
