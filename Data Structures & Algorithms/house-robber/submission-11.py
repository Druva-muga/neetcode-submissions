class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i in range(len(nums)):
            if i >= 2:
                dp[i] = max(nums[i]+dp[i-2],dp[i-1])
            else:
                dp[i] = max(nums[i],dp[i-1])

        return max(dp)

        