class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 1)
            return 0 ;

        int profit = 0 ; 
        int minStock = prices[0];

        for(int i  = 1 ; i < prices.size() ; i++){
            profit = max(profit ,prices[i] - minStock);
            if(minStock > prices[i])
                minStock = prices[i];
        }

        return profit;
        
    }
};