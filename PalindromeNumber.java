
import java.util.Scanner;
public class PalindromeNumber {
    static void palindrome(int n)
    {
        int temp=n;
        int rev=0;
        while(n>0)
        {
            int ld=n%10;
            rev=rev*10+ld;
            n=n/10;     
        }
        if (temp==rev) {
            System.out.println("TRUE");
        }
        else
        {
            System.out.println("FALSE");
        }
    }
    public static void main(String[] args) {
        palindrome(21);
    }
}
