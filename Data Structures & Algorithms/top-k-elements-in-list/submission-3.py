class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        freq = {}
        result = []
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for key,val in freq.items():
            bucket[val].append(key)
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

            

