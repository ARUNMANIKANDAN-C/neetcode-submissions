class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ct=0
        t =""
        for i in s:
            #print(t,i)
            if i not in t:
                t+=i
            else:
                p=t.index(i)
                ct=max(ct,len(t))
                t=t[p:]
        ct=max(ct,len(t))
        return ct