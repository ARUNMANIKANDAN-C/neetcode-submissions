class Solution:

    def encode(self, strs: List[str]) -> str:
        k=""
        for i in strs:
            k+=str(len(i))+"#" + i    
        return k
    def decode(self, s: str) -> List[str]:
        l=""
        strs=[]
        k=""
        kp=0
        while kp < len(s):
            m=int(s[kp])
            #print(m,s)
            for i in range(m):
                k+=s[kp+2+i]
                #print(k)
            strs.append(k)
            k=""
            kp=kp+2+m
        return strs
