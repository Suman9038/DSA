import java.util.*;
import java.math.*;
public class PowerSetUsingBitwiseOperator {
    static void Printpower(String str[])
    {
        int counter;
       int len=str.length;
       int powsize=(int)Math.pow(2,len);
       for( counter=0;counter<powsize;counter++)
       {
        for(int i=0;i<len;i++)
        {
            if((counter & 1<<i)!=0)
            {
                System.out.print(str[i]);
            }
        }
        System.out.println();
       }

    }
    public static void main(String[] args) {
        String str[]={"a","b","c"};
        Printpower(str);        
    }
}
