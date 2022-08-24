class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    list1 = ListNode()
    list1.val = 1
    list1.next = ListNode()
    list1.next.val = 2
    list1.next.next = ListNode()
    list1.next.next.val = 4

    list2 = ListNode()
    list2.val = 1
    list2.next = ListNode()
    list2.next.val = 3
    list2.next.next = ListNode()
    list2.next.next.val = 4
    output = ListNode()
    tail = output

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1 is not None:
        tail = list1
    elif list2 is not None:
        tail = list2
