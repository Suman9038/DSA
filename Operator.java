import java.util.Scanner;
public class Operator {
    public static void main(String[] args) {
        int x=3;
        //int y=6;
        int c=4; 
        int e=33;       
        // System.out.println(x & y);
        // System.out.println(x | y);
        // System.out.println(x ^ y);
        
        // LEFT SHUFT OPERATOR 

        // System.out.println(x << 1);
        // System.out.println(x << 2);
        // int d=(x<<c);
        // System.out.println(d);

        //RIGHT SHIFT OPERATOR
        System.out.println(e >> 1);
        System.out.println(e >> 2);
        int d=(e>>c);
        System.out.println(d);

        // BITWISE NOT OPERATOR(~) IN UNSIGNED
         int v=1;
        System.out.println(~v);

    }
}
