def goodNodes(root):
    def dfs(node, max_val):
        if not node:
            return 0

        if node.val >= max_val:
            max_val = node.val
            return 1 + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(node.left, max_val) + dfs(node.right, max_val)

    return dfs(root, root.val)
