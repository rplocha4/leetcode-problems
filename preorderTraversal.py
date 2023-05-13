def preorderTraversal(root):
    res = []

    def preorder(node):
        if node:
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    return res
