class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    head = ListNode()
    head.val = 1
    head.next = ListNode()
    head.next.val = 2
    head.next.next = ListNode()
    head.next.next.val = 3

    print("before reverse = ")
    print(head.val)
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    print(head.val)
