class Solution:
    def countSubstrings(self, s: str) -> int:
        reslen = 0
        palstr = ""

        for i in range(len(s)):
            r=i
            l=i
            while l>=0 and r<len(s) and s[l] == s[r]:
                reslen+=1
                r+=1
                l-=1
            r=i+1
            l=i
            while l>=0 and r<len(s) and s[l] == s[r]:
                reslen+=1
                r+=1
                l-=1

        return reslen

        