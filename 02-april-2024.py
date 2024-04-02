def inline(root,an):
    if(root.left):
        inline(root.left,an)
    an.append(root.data)
    if(root.right):
        inline(root.right,an)
    
class Solution:
    def absolute_diff(self,root):
        an=[]
        mi=float("inf")
        inline(root,an)
        for i in range(len(an)-1):
            mi=min(mi,abs(an[i]-an[i+1]))
        return(mi)