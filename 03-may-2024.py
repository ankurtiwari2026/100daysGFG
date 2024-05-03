class Solution:
    def KDistance(self,root,k):
        
        
        ans=[]
        q=deque()
        q.append(root)
        while q and k!=-1:
            for _ in range(len(q)):
                node=q.popleft()
                if k==0:
                    ans.append(node.data)
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            k-=1
        return ans