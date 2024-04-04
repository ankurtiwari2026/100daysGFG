class Solution:
    def kthCommonAncestor(self, root, k, x, y):
        # Code here
        if x == y:
            return -1
        l = []
        while root != None:
            l.append(root.data)
            if x < root.data and y < root.data:
                root = root.left
            elif x > root.data and y > root.data:
                root = root.right
            else:
                break
        if k > len(l): 
            return -1
        return l[len(l) - k]