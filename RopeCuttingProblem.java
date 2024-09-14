public class RopeCuttingProblem {
  static int Piece(int n,int a,int b,int c)
  {
    if(n==0)
    {
        return 0;
    }
    if(n<0)
    {
        return -1;
    }
    int res=Math.max(Math.max(Piece(n-a, a, b, c),Piece(n-b, a, b, c)),Piece(n-c ,a, b, c));
    if(res==-1)
    {
        return -1;
    }
    return res+1;
  }   
    public static void main(String[] args) {
        System.out.println(Piece(23, 11, 9, 12));
    }
    
}
