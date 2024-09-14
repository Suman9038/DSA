
import java.util.Scanner;
public class FactorialOfaNumber {
    // ITERATIVE APPROACH 
    // static void factorial(int n)
    // {
    //     int f=1;
    //     for(int i=1;i<=n;i++)
    //     {
    //         f=f*i;
    //     }
    //     System.out.println("THE FACTORIAL OF A NUMBER IS "+f);
    // }

    //  RECURSIVE APPROACH 
    static int factorial (int n)
    {
        if (n==0) {
            return 1;
        }
        else
        {
            return(n*factorial(n-1));
        }
    }
    public static void main(String[] args) {
        //factorial(5);
        System.out.println("THE FACTORIAL OF A NUMBER IS "+factorial(5));
    }
}
