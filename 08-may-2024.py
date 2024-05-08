class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        ans=[]
        rstack=[]
        self.dfs(root,ans,rstack)
        return ans
    def dfs(self,root,ans,rstack):
        rstack.append(root.data)
        if root.left:
            self.dfs(root.left,ans,rstack)
        if root.right:
            self.dfs(root.right,ans,rstack)
        if not (root.left or root.right):
            ans.append(rstack[:])
        rstack.pop()  