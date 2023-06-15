import collections


def maxLevelSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    q = collections.deque([root])
    max_val = float("-inf")
    level = 1
    min_level_val = 1
    while q:
        level_val = 0
        nodes_level = []
        while q:
            nodes_level.append(q.pop())

        for el in nodes_level:
            if el.left:
                q.append(el.left)
            if el.right:
                q.append(el.right)
            max_level += el.val

        if level_val > max_val:
            max_val = level_val
            min_level_val = level
        level += 1

    return min_level_val
