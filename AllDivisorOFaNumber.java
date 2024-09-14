
import java.util.Scanner;

public class AllDivisorOFaNumber {
    // NAIVE SOLUTION

    // static void divisor(int n)
    // {
    // for(int i=1;i<=n;i++)
    // {
    // if(n%i==0)
    // {
    // System.out.println(i);
    // }
    // }
    // }

    // EFFICIENT SOLUTION
    // THIS SOLUTION DOSNT PRINT IN SYSTAMICALLY
    // static void divisor(int n)
    // {
    // for(int i=1;i*i<=n;i++)
    // if(n%i==0)
    // {
    // System.out.println(i);
    // if(i!=(n/i)) // YE CONDITION CHECK KAREGA KI NUMBER VALUE OR i KA SQAURE
    // VALUE
    // // EQUAL HUA TOH WOO EK BAR PRINT KARDEGA OR DUBARA PRINT NHI KAREGA
    // {
    // System.out.println((n/i));
    // }
    // }
    // }
    static void divisor(int n) 
    {
        for (int i = 1; i * i < n; i++) {
            if (n % i == 0) {
                System.out.println(i);
            }
        }

        for (int i = (int) Math.sqrt(n); i >= 1; i--) 
        {
            if (n%i==0) // YE CONDITION CHECK KAREGA KI NUMBER VALUE OR i KA SQAURE VALUE
                              // EQUAL HUA TOH WOO EK BAR PRINT KARDEGA OR DUBARA PRINT NHI KAREGA
            {
                System.out.println((n / i));
            }
        }
    }

    public static void main(String[] args) {
        // divisor(6);
        // divisor(25);
        divisor(15);
    }
}
