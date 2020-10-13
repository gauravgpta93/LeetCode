"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import functools


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # return self.sol(root)
        return self.cleaner_sol(root)

    def sol(self, root):
        current = root
        while current:
            temp, first_child = self.get_next_child(current, None)
            # print(list(map(lambda x: x.val, child_list)))
            if not first_child:
                break
            current_node, current_child = temp, first_child
            while current_child:
                current_node, temp_child = self.get_next_child(current_node, current_child)
                current_child.next = temp_child
                current_child = temp_child
            current = first_child
        return root

    def get_next_child(self, node, child):
        while node:
            if node.right and child == node.right:
                node = node.next
                continue
            if node.left and child == node.left:
                if node.right:
                    return node, node.right

            if node.left and child != node.left:
                return node, node.left
            if node.right and child != node.right:
                return node, node.right
            node = node.next
        return node, None

    def cleaner_sol(self, root):
        start = root
        tail = dummy = Node(-1)
        while root:
            tail.next = None
            if root.left:
                tail.next = root.left
                tail = tail.next
            if root.right:
                tail.next = root.right
                tail = tail.next
            if root.next:
                root = root.next
            else:
                tail = dummy
                root = tail.next
        return start
