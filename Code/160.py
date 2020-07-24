# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        start_a, start_b = headA, headB
        swap_a = swap_b = False
        while headA and headB:
            if headA == headB:
                return headB
            if not headA.next:
                if swap_a:
                    return None
                headA = start_b
                swap_a = True
            else:
                headA = headA.next
            if not headB.next:
                if swap_b:
                    return None
                headB = start_a
                swap_b = True
            else:
                headB = headB.next

        return None
