class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<=len(s)-1:
                if s[l] == s[r]:
                    result = result+1
                else:
                    break
                l = l-1
                r = r+1
        for i in range(len(s)):
            l,r = i,i+1
            while l>=0 and r<=len(s)-1:
                if s[l] == s[r]:
                    result = result+1
                else:
                    break
                l = l-1
                r = r+1
        return result
