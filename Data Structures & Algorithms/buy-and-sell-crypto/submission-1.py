class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxright = [0]*len(prices)
        maxr = prices[len(prices)-1]
        result = 0
        for i in range(len(prices)-1,-1,-1):
            maxright[i]=maxr
            maxr = max(maxr,prices[i])
        for i in range(len(prices)):
            result = max(result,maxright[i]-prices[i])
        return result

