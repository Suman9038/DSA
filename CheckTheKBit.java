import java.util.Scanner;
public class CheckTheKBit {
    // FIRST METHOD IS USING LEFT SHIFT

    // static void kbit(int n,int k) {
    //     if((n & 1 << k-1)!=0)
    //     {
    //         System.out.println("YES");
    //     }
    //     else
    //     {
    //         System.out.println("NO");
    //     }
    // }

    // SECOND METHOD USING RIGHT SHIFT 
    static void kbit(int n,int k)
    {
        if(((n >> k-1) & 1)==1)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");

        }
    }

    public static void main(String[] args) {
        // kbit(5,3);
        kbit(13,3);
    }

}
