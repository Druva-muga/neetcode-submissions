class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [0]*len(nums)
        dp2 = [0]*len(nums)
        if(len(nums) == 1):
            return nums[0]
        max1,max2 = 0,0
        for i in range(len(nums)-1):
            if i>=2:
                dp1[i] = max(dp1[i-1],nums[i]+dp1[i-2])
            else:
                dp1[i] = max(dp1[i-1],nums[i])
                print(i,nums[i],dp1[i])
        max1 = max(dp1)

        for i in range(1,len(nums)):
            if i>=2:
                dp2[i] = max(dp2[i-1],nums[i]+dp2[i-2])
            else:
                dp2[i] = max(dp2[i-1],nums[i])
        max2 = max(dp2)
        return max(max1,max2)
        