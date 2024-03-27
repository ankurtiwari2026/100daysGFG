class Solution:
    def isAdditiveSequence(self, st):
        n=len(st)
        for i in range(n):
            for j in range(i+1,n):
                s,e=st[:i+1],st[i+1:j+1]
                ind=j+1
                re=str(int(s)+int(e))
                le=len(re)
                # if(ind==2):
                #     print(s,e,re,st[ind:ind+le])
                while(re==st[ind:ind+le]):
                    s,e=e,re
                    ind+=le
                    re=str(int(s)+int(e))
                    le=len(re)
                    # print(s,e,re,st[ind:ind+le],ind,22222)
                    if(ind==len(st)):
                        return(1)
                    elif(ind>len(st)):
                        break
        return(0)