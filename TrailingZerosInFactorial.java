
import java.util.Scanner;
public class TrailingZerosInFactorial {
    // NAIVE METHOD
    // IS METHOD KA TIME COMPLEXITY 0(n) H
    // PAR ISME OVERFLOW HO SKTA H   
    // static void trailingzeros(int n)
    // {
    //     int res=0;
    //     int f=1;
    //     for(int i=1;i<=n;i++)
    //     {
    //         f=f*i;
    //     }
    //     while(f%10==0)
    //     {
    //         res++;
    //         f=f/10;
    //     }
    //     System.out.println("THE TRAILING ZEROS ARE "+res);
    // } 

    // EFFECIENT SOLUTION 
    // TIME COMPLEXTY OF THIS SOLN IS 0(log n)
    static void trailingzeros(int n)
    {
        int res=0;
        for(int i=5;i<n;i=i*5)
        {
            res=res+(n/i);
        }
        System.out.println("THE TRAILING ZEROS ARE "+res);
    }
    public static void main(String[] args) {
       // trailingzeros(10);
       trailingzeros(251);   
    }
}
