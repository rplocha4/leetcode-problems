import collections


def rightSideView(root):
    res = []
    q = collections.deque([root])

    while q:
        right = None

        for i in range(len(q)):
            node = q.popleft()
            if node:
                right = node
                q.append(node.left)
                q.append(node.right)
        if right:
            res.append(right.val)

    return res
