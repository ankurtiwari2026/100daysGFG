
from typing import Optional
from collections import deque
from bisect import bisect_right


class Solution:
    def pairsViolatingBST(self, n, root):
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.data] + inorder(root.right)

        inorder_list = inorder(root)
        if len(inorder_list) <= 1:
            return 0

        ans = 0
        seen = []
        for val in inorder_list:
            pos = bisect_right(seen, val)
            ans += len(seen) - pos
            seen.insert(pos, val)

        return ans