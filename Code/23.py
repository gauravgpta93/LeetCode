# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        total_lenght = current_lenght = len(lists)
        if total_lenght <= 0:
            return ListNode()
        import math
        while current_lenght // 2 > 0:

            current_lenght = math.ceil(current_lenght / 2)
            print(current_lenght)
            for i in range(current_lenght):
                if 2 * i == current_lenght+1:
                    lists[i] = lists[2 * i]
                else:
                    lists[i] = self._merge_2_lists(lists[2 * i], lists[2 * i + 1])
            lists = lists[:current_lenght]
        return lists[0]

    def _merge_2_lists(self, l1, l2):
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
