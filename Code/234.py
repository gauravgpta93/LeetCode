# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s1 = list()
        slow = fast = head
        while fast and fast.next:
            s1.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if s1.pop() != slow.val:
                return False
            slow = slow.next
        return True
