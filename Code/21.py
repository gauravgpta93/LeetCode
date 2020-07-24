# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = current = ListNode(-1)
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    ans.next = l1
                    ans = ans.next
                    l1 = l1.next
                else:
                    ans.next = l2
                    ans = ans.next
                    l2 = l2.next
            else:
                while not l1 and l2:
                    ans.next = l2
                    ans = ans.next
                    l2 = l2.next
                while not l2 and l1:
                    ans.next = l1
                    ans = ans.next
                    l1 = l1.next
        return current.next