public class LargestElementInArray {
    // NAIVE METHOD
    static void Bigger(int arr[]) {
        int n = arr.length;
        int i;
        boolean flag;
        for (i = 0; i < n; i++) {
            flag = true;
            for (int j = 0; j < n; j++) {

                if (arr[j] > arr[i]) {
                    flag = false;
                    break;
                }
            }
        
        if (flag == true) {
            System.out.println(i);
        }
    }
}

//EFFECIENT SOLUTION 
static void getLargest(int arr[])
{
    int largest=0;
    for(int i=0;i<arr.length;i++)
    {
        if(arr[i]>arr[largest])
        {
            largest=i;
        }
    }
    System.out.println("THE LARGEST ELEMENT INDEX IS "+largest);
}

    public static void main(String[] args) {
        int arr[] = { 10, 5, 20, 8 };
        //Bigger(arr);
        getLargest(arr);
    }

}
