class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r,l=0,0
        maximum=0
        while(r<len(prices)): 
            if prices[l]<(prices[r]):
                maximum=max(maximum,prices[r]-prices[l])
            else:
                l=r
            r=r+1
        return maximum