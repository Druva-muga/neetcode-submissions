class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        n=len(nums)
        k=0
        while l<r:
            mid=(l+r)//2
            if(nums[mid]<nums[r]):
                r=mid
            else:
                l=mid+1
        k=l
        print(k)
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if(target>nums[(mid+k)%n]):
                l=mid+1
            elif(target<nums[(mid+k)%n]):
                r=mid-1
            else:
                return (mid+k)%n
        return -1


