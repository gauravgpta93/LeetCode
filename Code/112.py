# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.get_sum(root, 0, sum) if root else False

    def get_sum(self, root, current_sum, target):
        current_sum += root.val
        if not root.left and not root.right:
            return True if current_sum == target else False
        left_valid = self.get_sum(root.left, current_sum, target) if root.left else False
        right_valid = self.get_sum(root.right, current_sum, target) if root.right else False
        return left_valid or right_valid
