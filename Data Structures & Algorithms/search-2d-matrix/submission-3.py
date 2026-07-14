class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)-1
        n=len(matrix[0])-1
        l=0
        r=m
        while l<=r:
            mid = (r+l)//2
            if(matrix[mid][n]<target):
                l=mid+1
            elif(matrix[mid][0]>target):
                r=mid-1
            else:
                break
        if not(l<=r):
            return False
        mid=(l+r)//2
        l1=0
        r1=n
        while l1<=r1:
            mid1 = (l1+r1)//2
            if(matrix[mid][mid1]<target):
                l1=mid1+1
            elif(matrix[mid][mid1]>target):
                r1=mid1-1
            else:
                return True
        return False

