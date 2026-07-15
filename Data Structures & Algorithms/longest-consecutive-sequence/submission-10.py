class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct = set()
        length = 0
        result = 0
        for i in nums:
            distinct.add(i)
        for i in nums:
            length = 0
            if i-1 not in distinct:
                while length+i in distinct:
                    length+=1
            result = max(length,result)
        return result
        