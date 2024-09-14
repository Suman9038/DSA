public class RemoveDuplicatesFromASortedArray {
    //NAIVE SOLUTION
    static int remDups(int arr[],int n)
    {
        int temp[]=new int[n];
        temp[0]=arr[0];
        int res=1;
        for(int i=1;i<n;i++)
        {
            if(temp[res-1]!=arr[i])
            {
                temp[res]=arr[i];
                res++;
            }
        }
        for(int i=0;i<n;i++)
        {
            arr[i]=temp[res];
        }
        return res;
    }

    //EFFECIENT SOLUTION
    static int duplicate(int arr[])
    {
        int res=1;
        for(int i=1;i<arr.length;i++)
        {
            if(arr[res-1]!=arr[i])
            {
                arr[res]=arr[i];
                res++;
            }
        }
        return res;

    }
    public static void main(String[] args) {
        int arr[]={10,20,20,30,30,30};
        int n=arr.length;
        // System.out.println(remDups(arr, n));
        System.out.println(duplicate(arr));
    }
    
}
