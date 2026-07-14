class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l=0
        maxx=0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            maxx=max(maxx,r-l+1)
        return maxx
            
                
            
        