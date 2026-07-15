class Solution:
    def isPalindrome(self, s: str) -> bool:
        sarray = s.split(" ")
        finalstring = ''.join(sarray)
        finalstring = finalstring.lower()
        print(finalstring)
        i,j=0,len(finalstring)-1
        while i<j:
            if not (finalstring[i].isalpha() or finalstring[i].isalnum()):
                i+=1
            if not (finalstring[j].isalpha() or finalstring[j].isalnum()):
                j-=1
            if finalstring[i] != finalstring[j] and i<j:
                return False
            i+=1
            j-=1
        return True
        

        