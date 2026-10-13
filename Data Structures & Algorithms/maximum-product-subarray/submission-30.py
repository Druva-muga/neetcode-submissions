class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini = 1
        maxi = 1
        result = max(nums)
        for i in range(0,len(nums)):
            if nums[i] == 0:
                mini = 1
                maxi = 1
            temp = maxi
            maxi = max(mini*nums[i],maxi*nums[i],nums[i])
            mini = min(mini*nums[i],temp*nums[i],nums[i])
            result = max(result,maxi)
        return result