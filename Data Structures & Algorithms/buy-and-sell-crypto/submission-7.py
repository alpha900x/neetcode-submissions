class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        profit = 0
        while j<len(prices):
            while j<len(prices) and prices[i]>=prices[j]:
                i=j
                j+=1
                print(i,j)
            while j<len(prices) and prices[i]<prices[j] :
                profit = max(profit,prices[j] - prices[i])
                j=j+1
                print(i,j)
        return profit
                
            


            
            
            