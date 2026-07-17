class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        maxl ,maxr = 0,0
        result = 0
        while l<r:
            result = max(result,min(heights[l],heights[r])*(r-l))
            if heights[l]>heights[r]:
                r-=1
            elif heights[l]<heights[r]:
                l+=1
            else:
                l+=1
        return result

            
        