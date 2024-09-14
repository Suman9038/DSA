public class PalindromeChcekUsingRecursion {
     static boolean isPalindrome(String str,int start,int end)
     {
        if(start>=end)
        {
            return true;
        }
        return((str.charAt(start)==str.charAt(end)) && isPalindrome(str, start+1, end-1));
     }
    public static void main(String[] args) {
        String str="abbcbba";
        int start=str.length();
        int end=str.length()-1;
        System.out.println(isPalindrome(str, start, end));
    }
    
}
