
class Solution:
    def zigZagTraversal(self, root):
        q = deque([root])
        temp, resnodes = [], [root]
        
        level = 0       # root at level 0
        while q:
            node = q.popleft()
            
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            
            if not q:    # level is finished 
                level += 1
                q.extend(temp)
                
                # nodes at odd level are backwards
                resnodes = resnodes + temp[::-1] if level%2==1 else resnodes + temp
                # for next level nodes
                temp = []   
        
        resdata = [node.data for node in resnodes]
        return resdata
