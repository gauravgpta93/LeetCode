# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cycle_node = self.get_cycle_node(head)
        if not cycle_node:
            return None
        cycle_lenght = self.get_cycle_lenght(cycle_node)
        current = head
        while cycle_lenght > 1:
            cycle_lenght -= 1
            current = current.next
        current = current.next
        while head != current:
            head = head.next
            current = current.next
        return head

    def get_cycle_lenght(self, head):
        count = 1
        current = head.next
        while current and current != head:
            current = current.next
            count += 1
        return count

    def get_cycle_node(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next.next
        return None
