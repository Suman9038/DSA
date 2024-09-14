public class TowerOfHanoi {
    static void TOH(int n,char A, char B,char C)
    {
        if(n==1)
        {
            System.out.println("MOVE 1 FROM \t" + A +"\tTO\t"+C);
            return;
        }
        TOH(n-1,A,C,B);
        System.out.println("MOVE\t"+n+"\tFROM\t"+A+"\tTO\t"+C);
        TOH(n-1,B,A,C);

    }
    public static void main(String[] args) {
        TOH(3, 'A', 'B', 'C');
    }
    
}
