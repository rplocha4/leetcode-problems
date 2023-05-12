import collections


def levelOrder(root):
    res = []
    q = collections.deque([root])

    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                level.append(node.val)
        if level:
            res.append(level)
    return res
