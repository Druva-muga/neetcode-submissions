class Solution:
    def longestPalindrome(self, s: str) -> str:
        palstr = ""
        reslen = 0
        for i in range(len(s)):
            r=i
            j=i
            while i>=0 and j<len(s) and s[i] == s[j]:
                if((j-i+1) > reslen):
                    palstr = s[i:j+1]
                    reslen = j-i+1
                i-=1
                j+=1
            
            i=r
            j=r+1
            while i>=0 and j<len(s) and s[i] == s[j]:
                if((j-i+1) > reslen):
                    palstr = s[i:j+1]
                    reslen = j-i+1
                i-=1
                j+=1

        return palstr







        

        