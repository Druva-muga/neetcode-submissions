class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,cur,total):
            if target == total:
                res.append(cur.copy())
                return
            elif i >= len(candidates) or total>target:
                return
            
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            cur.pop()
            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return res

        # def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # res = []
        # def dfs(i,curr,total):
        #     if total == target:
        #         res.append(curr.copy())
        #         return
        #     elif total>target or i>=len(nums):
        #         return
            
        #     curr.append(nums[i])
        #     dfs(i,curr,total+nums[i])

        #     curr.pop()
        #     dfs(i+1,curr,total)
        # dfs(0,[],0)
        # return res
            
        