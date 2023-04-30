def isSubtree(root, subRoot):
    if not subRoot:
        return True
    if not root:
        return False

    def isSameTree(r, s):

        if not r and not s:
            return True
        if not r or not s:
            return False
        if (
            r.val == s.val
            and isSameTree(r.left, s.left)
            and isSameTree(r.right, s.right)
        ):
            return True
        else:
            return False

    if isSameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
