
class Solution:
    def findMaxForN(self, root, n):
                #code here
        res = -1
        while root is not None:
            if root.key == n:
                return n
            elif root.key < n:
                res = root.key 
                root = root.right
            else:
                root = root.left 
        return res