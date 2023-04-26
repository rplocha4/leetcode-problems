def hasCycle(head):
    if not head:
        return False
    slow = head
    fast = head.next

    while fast and fast.next:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False
