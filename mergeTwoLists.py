class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mertgeTwoLists(list1, list2):
    res = ListNode()
    pom = res

    while list1 and list2:
        if list1.val < list2.val:
            pom.next = list1
            list1 = list1.next
        else:
            pom.next = list2
            list2 = list2.next
        pom = pom.next

    if list1:
        pom.next = list1
    elif list2:
        pom.next = list2
    return res.next


