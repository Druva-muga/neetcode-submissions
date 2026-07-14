class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subs = {}
        for i in range(len(nums)):
            subs[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in nums and i != subs[target-nums[i]]:
                return [i,subs[target-nums[i]]]
        return []

        