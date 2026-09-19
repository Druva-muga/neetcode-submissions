class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        maxstr = ''
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<=(len(s)-1):
                if s[l] == s[r]:
                    if(maxlen != max(maxlen,(r-l)+1)):
                        maxstr = s[l:r+1]
                    maxlen = max(maxlen,(r-l)+1)
                else:
                    break
                r = r+1
                l = l-1
        for i in range(len(s)):
            l,r = i,i+1
            while l>=0 and r<=(len(s)-1):
                if s[l] == s[r]:
                    if(maxlen != max(maxlen,(r-l)+1)):
                        maxstr = s[l:r+1]
                    maxlen = max(maxlen,(r-l)+1)
                else:
                    break
                r = r+1
                l = l-1
        return maxstr

        