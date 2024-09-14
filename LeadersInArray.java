public class LeadersInArray {
    //NAIVE SOLUTION 
    static void LArray(int arr[], int n) {
        
        for (int i = 0; i < n; i++) {
            boolean flag = false; 
            for (int j = i + 1; j < n; j++) {
                if (arr[i] <= arr[j]) {
                    flag = true;
                    break;
                }

            }
            if (flag == false) {
                System.out.println(arr[i]);
            }
        }

    }
    //EFFECIENT SOLUTION

    static void Leader(int arr[],int n)
    {
        int curr_ldr=arr[n-1];
        System.out.println(curr_ldr);
        for(int i=n-2;i>=0;i--)
        {
            if(curr_ldr<arr[i])
            {
                curr_ldr=arr[i];
                System.out.println(curr_ldr);
            }
        }
    }

    public static void main(String[] args) {
        int arr[] = { 7,10,4,10,6,5,2 };
        int n = arr.length;
        LArray(arr, n);
        //Leader(arr, n);
    }

}
