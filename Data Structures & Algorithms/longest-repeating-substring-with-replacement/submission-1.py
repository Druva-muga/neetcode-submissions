class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        i=0
        j=0
        res=0
        freq[s[i]]=1
        while i<=j and j<len(s):
            print(freq)
            if ((j-i+1)-max(freq.values())) <= k:
                res = max(res,(j-i+1))
                j+=1
                if j<len(s):
                    freq[s[j]] = freq.get(s[j], 0) + 1
            else:
                freq[s[i]]-=1
                i+=1
        return res

                
