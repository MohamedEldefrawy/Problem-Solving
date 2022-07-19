class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve():
    head = ListNode()
    head.val = 1
    nodes_set = set()
    head.next = ListNode()
    head.next.val = 1
    head.next.next = ListNode()
    head.next.next.val = 1
    head.next.next.next = None
    curr = head
    while curr is not None:
        if curr in nodes_set:
            return True
        else:
            nodes_set.add(curr)
            curr = curr.next
    return False


def floyds_tortois_algorithm():
    head = ListNode()
    head.val = 1
    head.next = ListNode()
    head.next.val = 1
    head.next.next = ListNode()
    head.next.next.val = 1
    head.next.next.next = None

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


print(floyds_tortois_algorithm())
