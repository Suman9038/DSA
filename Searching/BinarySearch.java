package Searching;

public class BinarySearch {

    // NAIVE SOLUTION 
    static int linearSearch(int arr[],int x)
    {
        int n=arr.length;
        for(int i =0;i<n;i++)
        {
            if(x==arr[i])
            {
                return i;
            }
        }
        return -1;
    }
    //EFFECIENT SOLUTION 
    /*
     Sorted array k liya hume binary search use karna hoga unsorted array k liye 
     hum linear search use karenge sorted array k liye toh and uska worst case scenario 0(n) h 
     toh binary search use karenge for better optimisation 
     */
    static int binSearch(int arr[],int x)
    {
        int n=arr.length;
        int low =0;
        int high=n-1;
        while(low<=high)
        {
            int mid =(low+high)/2;
            if(arr[mid]==x)
            {
                return mid;
            }
            else if(arr[mid]>x)
            {
                high=mid-1;
            }
            else
            {
                low = mid+1;
            }
        }
        return -1;

    }

          //RECURSIVE SOLUTION 
    static int bSearch(int arr[],int low,int high,int x)
    {
        
        if(low>high)
        {
            return-1;
        }
            int mid = (low+high)/2;
            if(arr[mid]==x)
            {
                return mid;
            }
            else if(arr[mid]>x)
            {
               return(bSearch(arr, low, mid-1, x));
            }
            else
            {
                return(bSearch(arr, mid+1, high, x));
            }
    }

    public static void main(String[] args) {
        int arr[]={10,15,20};
        int x=203;
        int n=arr.length;
        int low=0;
        int high =n-1;
        // System.out.println(linearSearch(arr, x));
        // System.out.println(binSearch(arr, x));
        System.out.println(bSearch(arr,low,high, x));
    }
    
}
