def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def removeNthFromEnd(head, n):
    right = head
    tmp = ListNode(0, head)
    left = tmp
    for i in range(n):
        right = right.next

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return tmp.next
