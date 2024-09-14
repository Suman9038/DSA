public class CountSetBit {
    static int table[]=new int[256];
    // static void count(int n)
    // {
    // int count=0;
    // while(n>0)
    // {
    // if(n%2!=0)
    // {
    // count ++;
    // }
    // n=n/2;
    // }
    // System.out.println("THE NO OF SET IS "+count);
    // }

    // Brain Kerningams's Algorithm

    // static void count(int n)
    // {   
    //     int count=0;
    //     while(n>0)
    //     {
    //         n=(n&(n-1));
    //         count++;
    //     }
    //     System.out.println(count);
    // }

    //LOOKUP TABLE METHOD FOR 32 BITS NUMBER
    
    static void intializ()
    {
        table[0]=0;
        for(int i=0;i<256;i++)
        {
            table[i]=(i&1)+table[i/2];
        }

    }
    
    static void count(int n)
    {
        int count;
        count=table[n&0xff];
        n=n>>8;
        count=table[n&0xff];
        n=n>>8;
        count=table[n&0xff];
        n=n>>8;
        count=table[n&0xff];
        System.out.println(count);
    }

    public static void main(String[] args) {
        // count(7);
        //count(7);
        intializ();
        count(13);
    }

}
