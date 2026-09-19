class Solution:
    def numDecodings(self, s: str) -> int:
        allnums = set()
        for i in range(1,27):
            allnums.add(str(i))
        print(allnums)
        dp = [0]*len(s)
        for i in range(len(s)):
            if i == 0:
                if(s[i] == '0'):
                    return 0 
                dp[i] = 1
                continue
            if i == 1:
                if s[i-1:i+1] in allnums and s[i] in allnums:
                    dp[i] = 2
                elif s[i-1:i+1] in allnums and s[i] not in allnums:
                    dp[i] = 1
                elif s[i-1:i+1] not in allnums and s[i] in allnums:
                    dp[i] = 1
                continue
            if s[i] == '0' and s[i-1:i+1] in allnums:
                dp[i] = dp[i-2]
            elif s[i] == '0' and s[i-1:i+1] not in allnums:
                return 0
            elif s[i-1:i+1] in allnums and s[i] != '0':
                dp[i] = dp[i-1]+dp[i-2]
                print(i,dp[i-2])
            elif s[i-1:i+1] not in allnums:
                dp[i] = dp[i-1]
            
        print(dp)
        return dp[-1]