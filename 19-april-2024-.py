class Solution:
        
     def findMissing(self,a,b,n,m):
            s=set()
            l=[]
            for i in b:
                s.add(i)
            for i in a:
                if i not in s:
                    l.append(i)
            return l