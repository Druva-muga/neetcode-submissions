class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxfreq = 0
        i = 0
        result = 0
        for j in range(len(s)):
            freq[s[j]] = 1+freq.get(s[j],0)
            winlen = j-i+1
            if maxfreq<freq[s[j]]:
                maxfreq = freq[s[j]]
            if (winlen-maxfreq)<=k:
                result = max(result,winlen)
            else:
                freq[s[i]]-=1
                i+=1
            print(i,j,winlen,maxfreq)

        return result
        