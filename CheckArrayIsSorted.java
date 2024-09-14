public class CheckArrayIsSorted {
    //NAIVE METHOD
    static boolean Sorted(int arr[])
    {
        for(int i=0;i<arr.length;i++)
        {
            for(int j=i+1;j<arr.length;j++)
            {
                if (arr[j]<arr[i]) {
                    return false;
                }
            }
        }
        return true;
    } 

    //EFFECIENT SOLUTION
    static boolean isSorted(int arr[])
    {
        for(int i=1;i<arr.length;i++)
        {
            if(arr[i]<arr[i-1])
            {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        int arr[]={5,12,2,30,35};
        //System.out.println(Sorted(arr));
        System.out.println(isSorted(arr));
    }   
}
