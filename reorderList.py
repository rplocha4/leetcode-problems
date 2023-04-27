def reorderList(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    first, second = head, prev
    while second:
        first.next, first = second, first.next
        second.next, second = first, second.next
