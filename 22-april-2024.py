class Solution:
    def minRow(self,n,m,a):
        li=[]
        for i in a:
            li.append(i.count(1))
        return li.index(min(li))+1        
                