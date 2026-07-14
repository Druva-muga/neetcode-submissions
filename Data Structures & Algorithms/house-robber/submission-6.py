from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):
                return 0
            # Choose: rob this house and skip next OR skip this house
            return max(dfs(i + 1), nums[i] + dfs(i + 2))
        
        return dfs(0)
