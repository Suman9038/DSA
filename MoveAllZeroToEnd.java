public class MoveAllZeroToEnd {
    //NAIVE SOLUTION
    static void zero(int arr[])
    {
        int n=arr.length;
        for(int i=0;i<n;i++)
        {
            if(arr[i]==0)
            {
                for(int j=i+1;j<n;j++)
                {
                    if(arr[j]!=0)
                    {
                        int temp=arr[i];
                        arr[i]=arr[j];
                        arr[j]=temp;

                    }
                }
            }
        }
        for(int x=0;x<n;x++)
        {
            System.out.println(arr[x]);
        }
    }
    
    //EFFECIENT SOLN 
    static void moveTo(int arr[])
    {
        int count=0;
        int n=arr.length;
        for(int i =0;i<n;i++)
        {
            if(arr[i]!=0)
            {
                int temp=arr[i];
                arr[i]=arr[count];
                arr[count]=temp;
                count++;
            }
        }
        for(int x=0;x<n;x++)
        {
            System.out.println(arr[x]);
        }
    }
    public static void main(String[] args) {
         int arr[]={10,5,0,8,0,9,0};
         //zero(arr);
         moveTo(arr);
    }
    
}
