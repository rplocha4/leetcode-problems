def diameterOfBinaryTree(root):
    res = 0

    def maxDepth(node):
        nonlocal res
        if not node:
            return 0

        left = maxDepth(node.left)
        right = maxDepth(node.right)
        res = max(res, left + right)
        return 1 + max(left, right)

    maxDepth(root)
    return res
