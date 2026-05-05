class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        kp = len(s2)
        lp = len(s1)
        d =set(s1)
        dp =defaultdict()
        for i in s1:
            dp[i] = dp.get(i,0) +1
        k,l=0,lp
        while l<=kp :
            if d == set(s2[k:l]):
                dpp ={}
                for i in s2[k:l]:
                    dpp[i] = dpp.get(i,0) +1
                if dp ==dpp:
                    return True 
            else:
                k+=1
                l+=1
        return False