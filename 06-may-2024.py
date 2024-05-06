def noSibling(root):
    no_sibb = []
    def helper(node):
        if node:
            if node.left and not node.right:
                no_sibb.append(node.left.data)
            if node.right and not node.left:
                no_sibb.append(node.right.data)
            helper(node.left)
            helper(node.right)
    helper(root)
    return sorted(no_sibb) if no_sibb else [-1]
