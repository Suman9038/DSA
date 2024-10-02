public class MajorityElements {
    //NAIVE SOLUTION
    static void findMajority(int arr[])
    {
        int n=arr.length;
        for(int i =0;i<n;i++)
        {
            int count =1;
            for(int j=i+1;j<n;j++)
            {
                if(arr[i]==arr[j])
                {
                    count++;
                }
            }
            if(count>n/2)
            {
                System.out.println(i);
            }
        }
    }

    // EFFECIENT SOLN 

    static int find_Majority(int arr[])
    {
        int res=0;
        int count =1;
        int n= arr.length;
        for(int i =1; i<n;i++)
        {
            if (arr[res]==arr[i])
            {
                count++;
            }
            else
            {
                count--;
            }
            if(count == 0)
            {
                res=i;
                count=1;
            }
        }
        count=0;
        for(int i =0;i<n;i++)
        {
            if(arr[res]==arr[i])
            {
                count++;
            }
        }
        if(count<=n/2)
        {
            return -1;

        }
        return res;
    }
    public static void main(String[] args) {
        int arr[]={8,7,6,8,6,6,6,6};
    //     findMajority(arr);
        // int arr[]={8,8,6,6,4,6};
       System.out.println(find_Majority(arr)); 
    }
    
}
