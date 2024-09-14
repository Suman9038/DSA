import java.util.*;

public class TwoOddoccuringNumber {
    static void addAppearing(int arr[]) {
        int xor=0,res1=0,res2=0;
        int sn;
        for(int i =0;i<arr.length;i++)
        {
            xor=xor^arr[i];
        }
        sn=xor & ~(xor-1);// THIS SPECIFIC LINE IS FOR THE FINDING THE RIGHT MOST BIT
        for(int i=0;i<arr.length;i++)
        {
            if((arr[i]&sn)!=0)
            {
                res1=res1^arr[i];
            }
            else
            {
                res2=res2^arr[i];
            }
        }
        System.out.println(res1);
        System.out.println(res2);

    }

    public static void main(String[] args) {
        int arr[]={3,4,3,4,8,4,4,32,7,7};
        addAppearing(arr);
    }

}