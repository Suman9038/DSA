public class TailRecursion {
    //PRINT NO 1 TO N IS NOT TAIL RECURSIVE
    //WE CAN MAKE IT TARIL RECURSIVE BY MAKING SOME CHANGES
    static void fun(int n,int k)
    {
        if(n==0)
        {
            return;
        }
        System.out.println(k);
        fun(n-1,k+1);
    }
    // FACTORIAL OF A NO IS NOT TAIL RECURSIVE
    //WE CAN MAKE IT TARIL RECURSIVE BY MAKING SOME CHANGES 
    static int fun1(int n,int k)
    {
        if(n==0 || n==1)
        {
            return k;
        }
        return fun1(n-1,k*n);
    }
    public static void main(String[] args) {
        //fun(3, 1);
       System.out.println( fun1(3, 1));
    }
    
}
