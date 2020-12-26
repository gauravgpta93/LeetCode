# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.swap(head)

    def swap(self, head):
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swap(temp.next)
        temp.next = head
        return temp
