class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(nums[0],self.dfs(nums[1:]),self.dfs(nums[:-1]))

    def dfs(self,nums):
        rob1,rob2 = 0,0
        for i in nums:
            newrob = max(i+rob1,rob2)
            rob1 = rob2
            rob2 = newrob 
        return rob2
        