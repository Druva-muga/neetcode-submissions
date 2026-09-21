class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # we maintain current max and current min and current min is supposed to be negative and when a new negative values comes it is multiplied with current min and if the val of current min multiplied with current element is more than current max then that value is the current max and when zero comes we reset the values of current max and current min to 1 each
        currentmin = 1
        currentmax = 1
        result = max(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                currentmin,currentmax = 1,1
            else:
                temp = currentmax*nums[i]
                currentmax = max(currentmax*nums[i],currentmin*nums[i],nums[i])
                currentmin = min(temp,currentmin*nums[i],nums[i])
                result = max(result,currentmax)
              
        return result

        