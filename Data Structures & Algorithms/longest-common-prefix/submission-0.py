class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<1:
            return ""
        k=0
        l=""
        for i in range(len(strs[0])):
            t=strs[0][i]
            flag=True
            for j in strs[1:]:
                if t!=j[i]:
                    flag=False
            if flag==True:
                l=l+t
            else:
                return l