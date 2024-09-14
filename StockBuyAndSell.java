import java.math.*;
public class StockBuyAndSell {
    static int maxprofit(int price[],int start,int end)
    {
        if(end<=start)
        return 0;
        int profit=0;
        int curr_profit;
        for(int i=start;i<end;i++)
        {
            for(int j=i+1;j<=end;j++)
            {
                if(price[j]>price[i])
                {
                     curr_profit= price[j]-price[i] + maxprofit(price, i, i-1) + maxprofit(price, j+1, end);
                     profit=Math.max(profit,curr_profit);
                }
            }
        }
        return profit;
    }
    // EFFECIENT SOLUTION
    
    static int maxProfit(int profit[])
    {
        int n=profit.length;
        int profit=0;
        for(int i=1;i<n;i++)
        {
            if(profit[i]>profit[i-1])
            {
                profit=profit+(profit[i]-profit[i-1]);
            }
        }
        return profit;
    }
    public static void main(String[] args) {
        int arr[]={1,5,3,8,12};
        int start=0;
        int end=arr.length-1;
        //System.out.println(maxprofit(arr, start, end));
        System.out.println(maxProfit(arr));
    }
    
}
