class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicts = dict()
        dictt = dict()
        for i in range(len(s)):
            if s[i] not in dicts:
                dicts[s[i]] = 1
            if t[i] not in dictt:
                dictt[t[i]] = 1
            dicts[s[i]] += 1
            dictt[t[i]] += 1
        for i in s:
            if i in s and i in t:
                if dicts[i] != dictt[i]:
                    return False
            else:
                return False
        return True


        