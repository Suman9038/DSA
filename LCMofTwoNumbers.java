
import java.util.Scanner;
public class LCMofTwoNumbers {
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
    static int lcm(int a, int b)
    {
        return((a*b)/gcd(a,b));
    }
    public static void main(String[] args) {
        System.out.println(lcm(4, 6));
    }
}
