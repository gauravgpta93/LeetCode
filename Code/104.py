# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.get_depth(root, 0) if root else 0

    def get_depth(self, root, current):
        if not root:
            return current
        left_d = self.get_depth(root.left, current + 1)
        right_d = self.get_depth(root.right, current + 1)
        return max(left_d, right_d)