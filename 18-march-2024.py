class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        q=[root.data]
        values=[root]
        while (len(values)!=0):
            val=values.pop(0)
            if(val.left):
                q.append(val.left.data)
                values+=[val.left]
            if(val.right):
                q.append(val.right.data)
                values+=[val.right]
        return q        