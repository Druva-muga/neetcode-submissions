class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def dp(nums):
            dp=[0]*len(nums)
            for i in range(len(dp)):
                if i==0:
                    dp[0] = nums[0]
                elif i==1:
                    dp[1] = max(nums[0],nums[1])
                else:
                    dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            print(dp)
            return dp[-1]
        print(nums[0:-1],nums[1:len(nums)+1])
        return max(dp(nums[0:-1]),dp(nums[1:len(nums)+1]))
        