
import java.util.Scanner;
public class GCDofTwoNumber {
    // NAIVE SOLUTION 
    // static void gcd(int a, int b)
    // {
    //     int min;
    //     if(a<b)
    //     {
    //         min=a;
    //     }
    //     else
    //     {
    //         min=b;
    //     }
    //     while(min>0)
    //     {
    //         if(min%a==0 && min%b==0)
    //         {
    //             break;
    //         }
    //         else
    //         {
    //             min--;
    //         }
    //     }
    //     System.out.println("THE GCD OF THE TWO NUMBER IS"+min);
    // }

    // Optimized Euclidean Algorithm 
        static int gcd(int a, int b)
        {
            if(b==0)
            {
                return a;
            }
            else
            {
                return gcd(b,a%b);
            }
        }
    public static void main(String[] args) {
        System.out.println(gcd(10, 15));
        //gcd(4, 6);
    }
    
}
