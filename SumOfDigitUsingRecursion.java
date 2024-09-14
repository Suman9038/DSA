public class SumOfDigitUsingRecursion {
    static int sumdigit(int n)
    {
        if(n==0)
        {
            return 0;
        }
        return (n%10+sumdigit(n/10)); 
        

    }
    public static void main(String[] args) {
        System.out.println(sumdigit(873));
    }
    
}
