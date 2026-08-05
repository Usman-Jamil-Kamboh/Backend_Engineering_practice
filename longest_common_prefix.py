class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first_str = strs[0]
        output = ""

        for i in range(0 , len(first_str)):
            
            for a in range (1 , len(strs)):
                if len(strs[a]) <= i :
                    return output 

                if  strs[a][i] != first_str[i]:
                    return output 

            
            output += first_str[i]

        return output
