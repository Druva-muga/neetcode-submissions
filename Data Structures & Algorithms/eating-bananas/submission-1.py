class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=max(piles)
        while l<=r:
            mid=(l+r)//2
            hc=0
            for i in piles:
                hc = hc + math.ceil(i/mid)
            if(hc<=h):
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res