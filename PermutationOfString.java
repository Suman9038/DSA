public class PermutationOfString {
    public static void swap(String [] s, int i, int x) {
        String temp = s[i];
        s[i] = s[x];
        s[x] = temp;
      }
   static void permutre(String [] s, int i)
    {
        if(i==s.length-1)
        {
            System.out.println(s+" ");
        }
        for(int j =i;j<s.length;j++)
        {
        swap(s,i,j);
        permutre(s,i+1);
        swap(s,i,j);
        }
    }
    public static void main(String[] args) {
        String [] s={"ABC"};
        int i=0;
        permutre(s, i);
    }
    
}
