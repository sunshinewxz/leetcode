/*
My method: local optimum and global optimal solution
local[i+1] = max(local[i] + prices[i+1] - prices[i], 0)
global[i+1] = max(local[i+1], global[i])
*/
import static java.lang.Math.max;

public class Main {

    public static void main(String[] args) {
        int[] prices = {};
        int result = maxProfit(prices);
        System.out.println(result);
    }

    public static int maxProfit(int[] prices) {
        int len = prices.length;
        if (len<1)
            return 0;
        int[] local = new int[len];
        int result = 0;
        local[0] = 0;
        for (int i=0; i<len-1; i++){
            local[i+1] = max(local[i]+prices[i+1]-prices[i], 0);
            result = max(local[i+1],result);
        }
        return result;

    }

}

/*
Optimize the calculation process in the loop
*/

import static java.lang.Math.max;
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0, buy = Integer.MAX_VALUE;
        for (int price : prices) {
            buy = Math.min(buy, price);
            res = Math.max(res, price - buy);
        }
        return res;
    }
}