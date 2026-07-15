class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        distinct = set()
        for i in nums:
            distinct.add(i)
        maxlen=0
        j=0
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            maxcurr = 0
            j=nums[i]
            while True:
                maxcurr+=1
                if j not in distinct:
                    break
                print(j,maxcurr)
                maxlen = max(maxlen,maxcurr)
                visited.add(j+1)
                j+=1
        return maxlen
        