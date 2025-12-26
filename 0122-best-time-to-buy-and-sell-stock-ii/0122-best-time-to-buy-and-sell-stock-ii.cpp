class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;

        int low = prices[0];
        int high = prices[0];
        int i= 0;
        int n =prices.size();
        while(i < n - 1){
            while(i < n -1  && prices[i] >= prices[i+1])
                i+=1;
            low = prices[i];
            while(i < n -1  && prices[i] <= prices[i+1])
                i+=1;
            high = prices[i];

            profit += (high-low);

        }
        return profit;
    }
};