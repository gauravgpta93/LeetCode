"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # return self.extra_space(root)
        return self.without_extra_space(root)

    def extra_space(self, root):
        queue = list()
        queue = [root, None]
        prev = None
        while queue:
            temp = queue.pop(0)
            if not prev and not temp:
                break
            if not temp:
                prev.next = None
                prev = None
            else:
                queue.append(temp.left)
                queue.append(temp.right)
                if queue[0] == None:
                    queue.append(None)
                if prev:
                    prev.next = temp
                prev = temp

        return root

    def without_extra_space(self, root):
        current = root
        while current and current.left:
            temp = current.left
            while current:
                current.left.next = current.right
                current.right.next = current.next.left if current.next else None
                current = current.next
            current = temp
        return root
