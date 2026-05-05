class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        k = {'+':1,'-':2,'*':3,'/':4}
        l=[]
        for i in tokens:
            #print(l)
            if i in k:
                p=l.pop()
                m=l.pop()
                ki=k[i]
                if ki==1:
                    o=p+m
                elif ki==2:
                    o=m-p
                elif ki==3:
                    o=p*m
                else:
                    o=m/p
                l.append(o)
            else:
                l.append(int(i))
        #print(l)
        return int(l[0])