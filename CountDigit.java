
public class CountDigit {
    //ITERATIVE APPROACH 
    
    static void countdigit(int x)
    {
        int count=0;
        while(x>0)
        {
            x=x/10;
            count++;
        }
        System.out.println("THE COUNTED NUMBER IS "+ count);
    }
    public static void main(String[] args) {
        countdigit(123);
    }
}
