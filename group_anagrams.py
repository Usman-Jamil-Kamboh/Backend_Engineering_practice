class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}
        
        for s in strs:
            sort = "".join(sorted(s))
            if sort in result:
                result[sort].append(s)
            else:
                result[sort] = [s]
        
        return list(result.values())



        
