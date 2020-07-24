# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        reverse_start = self._reverse_list(slow.next)
        slow.next = None
        # print(reverse_start)
        self._join(head, reverse_start)

    def _reverse_list(self, head):
        if not head or not head.next:
            return head
        temp = self._reverse_list(head.next)
        head.next.next = head
        head.next = None
        return temp

    def _join(self, head_1, head_2):
        while head_1 and head_2 and head_2 != head_1.next:
            print(head_1.val, head_2.val)
            print(head_1, head_2)
            # head_1, head_1.next, head_2, head_2.next = head_1.next, head_2, head_2.next, head_1.next
            temp_1, temp_2 = head_1.next, head_2.next
            head_1.next = head_2
            head_2.next = temp_1
            head_1 = temp_1
            head_2 = temp_2

        if head_1:
            head_1.next = None
