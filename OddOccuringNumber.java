import java.util.*;
public class OddOccuringNumber {
    static int findOdd(int arr[])
    {
        int res=0;
        for(int i=0;i<arr.length;i++)
        {
            res=res^arr[i];
        }
        return res;
    }
    static void  MissingNumber(int arr[])
    {
        int a=arr[0];//For xor of all the elements in array
        int b=1;
        //
        for(int  i =1;i<arr.length;i++)
        {
            a=a^arr[i];
        }
        for( int i =2;i<=arr.length+1;i++)// For xor of all the elements from 1 to n+1
        {
            b=b^i;
        }
        System.out.println(a^b);
    }
    public static void main(String[] args) {
        int arr[]={1,5,3,2};
        // NAIVE METHOD

    //     for(int i=0;i<arr.length;i++ )
    //     {
    //         int count=0;
    //         for(int j=0;j<arr.length;j++)
    //         {
    //             if(arr[i]==arr[j])
    //             {
    //                 count++;
    //             }
    //         }
    //         if(count%2!=0)
    //         {
    //             System.out.println(arr[i]);
    //         }  
    //     }    
           
    // }
    // System.out.println(findOdd(arr));
        MissingNumber(arr);
}
}
