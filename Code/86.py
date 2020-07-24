# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ans = less = ListNode(-1)
        more_start = more = ListNode(-1)
        current = head
        while current:
            if current.val < x:
                less.next = current
                current = current.next
                less = less.next
                less.next = None
            else:
                more.next = current
                current = current.next
                more = more.next
                more.next = None

        less.next = more_start.next
        return ans.next