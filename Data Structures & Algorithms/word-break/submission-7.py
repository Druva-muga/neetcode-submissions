class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)

        def solve(s):
            if s == "":
                return True

            if s in memo:
                return memo[s]

            for i in range(1, len(s) + 1):
                word = s[:i]

                if word in wordSet and solve(s[i:]):
                    memo[s] = True
                    return True

            memo[s] = False
            return False

        return solve(s)