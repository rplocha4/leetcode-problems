def inorderTraversal(root):
    res = []

    def inorder(node):
        if node:
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return res
