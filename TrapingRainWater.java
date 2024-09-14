public class TrapingRainWater {
    // NAIVE SOLUTION 
    static void getwater(int arr[])
    {
        int n=arr.length;
        int res=0;
        for(int i=1;i<n-1;i++)
        {
        int lmax=arr[i];
        for(int j=0;j<i;j++)
        {
            lmax= (Math.max(lmax,arr[j]));
        }
        int rmax=arr[i];
        for(int j=i+1;j<n;j++)
        {
            rmax=(Math.max(rmax, arr[j]));
        }
        res=(res+ Math.min(lmax, rmax))-arr[i];
        }
        System.err.println(res);
    }
    // EFFECIENT SOLUTION
    static void getWater(int arr[])
    {
        int n= arr.length;
        int res=0;
        int lmax[]= new int[n]; // for storing the pre calculated max left most for the every element for i 
        int rmax[]= new int[n]; // for storing the pre calculated max right most for the every element for i 
        lmax[0]=arr[0];
        for(int j=1;j<n;j++)
        {
            lmax[j]=(Math.max(arr[j],lmax[j-1]));
            //System.err.println("ALL THE MAXIMUM VALUE OF THE LEFT MOST BAR OF EACH iTH ELEMENT "+lmax[j]);
        }
        rmax[n-1]=arr[n-1];
        for(int j=n-2;j>=0;j--)
        {
            rmax[j]=(Math.max(arr[j],rmax[j+1]));
            //System.err.println("ALL THE MAXIMUM VALUE OF THE RIGHT  MOST BAR OF EACH iTH ELEMENT "+rmax[j]);
        }
        for(int i=1;i<n-1;i++)
        {
            res= res+(Math.min(lmax[i], rmax[i]))-arr[i];
        }
        System.out.println(res);
    }
    public static void main(String[] args) {
        int arr[]={5,0,6,2,3};
        // getwater(arr);
        getWater(arr);

    }
    
}
