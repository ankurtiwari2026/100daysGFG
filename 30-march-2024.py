class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        current=root
        while current.left is not None:
            current=current.left
        return current.data    
     