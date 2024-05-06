class Solution:
    def buildTree(self,In, post, n):
        if len(In):
            node = Node(post.pop())
            ind = In.index(node.data)
            node.right = self.buildTree(In[ind + 1:],post,n)
            node.left = self.buildTree(In[:ind],post,n)
            
            return node
        else:
            return None