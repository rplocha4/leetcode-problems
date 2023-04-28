def isSameTree(p, q):
    if p == None and q == None:
        return True
    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    else:
        return False
