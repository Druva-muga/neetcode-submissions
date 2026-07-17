class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        distinct = set()
        if len(s) == 0:
            return 0
        distinct.add(s[l])
        result = 1
        while l<=r and r<len(s)-1:
            r+=1
            print((r-l)+1,s[r],distinct)  
            if s[r] not in distinct:
                result = max((r-l)+1,result)
                distinct.add(s[r])
            elif s[r] in distinct:
                while s[l]!=s[r] and l<r:
                    distinct.remove(s[l])
                    l+=1
                l+=1
        return result



        