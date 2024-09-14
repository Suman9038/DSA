public class OperatorInArray {
    static int search(int arr[],int x)
    {
        for(int i =0;i<arr.length;i++)
        {
            if (arr[i]==x) {
                return i;
            }
        }
        return -1;
    }
    
    static int insert(int arr[],int x,int pos,int cap)
    {   
        int newarr[]=new int[arr.length+1];
        if(arr.length==cap)
        {
            return cap;
        }
        int idx=pos-1;
        for( int i =arr.length-1;i>=idx;i--)
        {
            newarr[i+1]=newarr[i];
        }
        newarr[idx]=x;
        return (arr.length+1);
    }
    static void delete(int arr[],int x,int n)
    {
        int i;
        for( i =0;i<arr.length;i++)
        {
            if (arr[i]==x) {
                System.out.println("ELMENT IS FOUND WHICH SHOULD BE DELETED");
            }
        }
        if(n==arr.length)
        {
            System.out.println(n);
        }
        for(int j=i;j<n-1;j++)
        {
            arr[j]=arr[j+1];
        }
        System.out.println(arr.length-1);
    }
    public static void main(String[] args) {
        // int cap=5;
        int arr[]={20,5,7,25};
        // System.out.println(search(arr, 5));
        // System.out.println(search(arr, 15));
        // System.out.println(insert(arr, 3, 2, cap));
        delete(arr, 5, arr.length);

    }
    
}
