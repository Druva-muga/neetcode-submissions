class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack =[]
        for i,j in enumerate(heights):
            pos=i
            while stack and stack[-1][0]>j:
                height,pos = stack.pop()
                maxarea=max(maxarea,(i-pos)*height)
            stack.append([j,pos])
        while stack:
            heightE,posE = stack.pop()
            maxarea = max(((len(heights)-posE)*heightE),maxarea)
        return maxarea

        