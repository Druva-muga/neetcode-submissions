class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        k1 = k
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        for key,fre in sorted_dict.items():
            k1-=1
            if k1<0:
                break
            result.append(key)
            print(key,k1)
        return result
            
            
        

            
        