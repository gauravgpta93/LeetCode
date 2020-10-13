# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        in_order_dict = dict(zip(inorder, range(len(inorder))))
        return self.build_tree(in_order_dict, preorder, 0, len(inorder) - 1)

    def build_tree(self, in_order_dict, preorder, left, right):
        if left > right:
            return None
        mid = preorder.pop(0)
        temp = TreeNode(mid)
        mid_index = in_order_dict[mid]
        temp.left = self.build_tree(in_order_dict, preorder, left, mid_index - 1)
        temp.right = self.build_tree(in_order_dict, preorder, mid_index + 1, right)
        return temp
