# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = ans = ListNode(-1)
        current = head
        while current:
            if current and current.next and current.next.val == current.val:
                while current and current.next and current.next.val == current.val:
                    current.next = current.next.next
                current = current.next
            else:
                prev.next = current
                prev = prev.next
                current = current.next if current else None
        return ans.next
