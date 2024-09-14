

public class expo {
    static int p(int x,int n)
    {
        if(n==0)
        {
            return 1;
        }
        int temp=p(x,n/2);
        temp=temp*temp;
        if(n%2==0)
        {
            return temp;
        }
        else{
            return temp*x;
        }
    }
    public static void main(String[] args) {
        p(2, 3);
    }    
}
