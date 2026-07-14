class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"qprs","8":"tuv","9":"wxyz"}
        def concat(i,cstring):
            if len(cstring) == len(digits):
                res.append(cstring)
                return
            for j in dic[digits[i]]:
                concat(i+1,cstring+j)

        if digits:
            concat(0,"")
        return res
            


