import java.util.*;

public class PowerOfTwo {
    // static boolean isPow(int n) {
    //     if (n == 0) {
    //         return false;
    //     }
    //     while (n != 1) {
    //         if (n % 2 != 0) {
    //             return false;
    //         }
    //         n = n / 2;
    //     }
    //     return true;
    // }

    // EFFICEINT METHOD

     static boolean isPow(int n)
     {
        if(n==0)
        {
            return false;
        }
        return ((n & n-1)==0);

     }

    public static void main(String[] args) {
        // System.out.println(isPow(4));
        System.out.println(isPow(6   ));

    }
}
