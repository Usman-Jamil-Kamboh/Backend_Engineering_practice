class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       minimum_price = prices[0]
       profit = 0 
       for i in prices[1 :]:
            profit = max(profit , i - minimum_price)
            minimum_price = min(minimum_price , i )
       return profit
            
