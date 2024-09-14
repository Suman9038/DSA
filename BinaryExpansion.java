
import java.util.*;
import java.lang.Math;;
public class BinaryExpansion {
    static void binary(int x, int n)
    {
        int res=1;
        while (n>0) {
            if(n%2!=0)
            {
                res=res*x;
            }
            x=x*x;
            n=n/2;
        }
        System.out.println(res);
    }
    public static void main(String[] args) {
        binary(2, 2);
    }
}