# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n <= 0:
            return None
        forward = 0
        current = head
        while forward < n:
            current = current.next
            forward += 1
        ans = back = ListNode(-1)
        ans.next = head
        while current:
            current = current.next
            back = back.next
        back.next = back.next.next
        return ans.next
