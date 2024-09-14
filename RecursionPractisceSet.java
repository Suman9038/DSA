public class RecursionPractisceSet {
    // static void fun(int n)
    // {
    //     if(n==0)
    //     {
    //         return;
    //     }
    //     System.out.println(n);
    //     fun(n-1);
    //     System.out.println(n);
    // }

    // static void fun(int n)
    // {
    //     if(n==0)
    //     {
    //         return;
    //     }
    //     fun(n-1);
    //     System.out.println(n);
    //     fun(n-1);
    // }
    static int fun(int n)
    {
        if(n==1)
        {
            return 0;
        }
        else
        {
            return 1+fun(n/2);
        }
    }
    public static void main(String[] args) {
            // fun(3);     
            System.out.println( fun(16)  );
    }
}
