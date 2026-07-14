class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictlist = {}
        result = []
        for str1 in strs:
            sortedstr = "".join(sorted(str1))
            if sortedstr not in dictlist:
                dictlist[sortedstr] = []
            dictlist[sortedstr].append(str1)
        
        for key , item in dictlist.items():
            result.append(item)
        return result
            

        