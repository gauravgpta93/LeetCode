# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        in_order_dict = dict(zip(inorder, range(len(inorder))))
        return self.build_sub_tree(postorder, in_order_dict, 0, len(inorder) - 1)

    def build_sub_tree(self, post_order, in_order_dict, start, end):
        if start > end:
            return None
        # post_order = list(filter(lambda x: x in in_order, post_order))
        node_val = post_order.pop()
        center_index = in_order_dict[node_val]
        right_tree = self.build_sub_tree(post_order, in_order_dict, center_index + 1, end)
        left_tree = self.build_sub_tree(post_order, in_order_dict, start, center_index - 1)
        temp = TreeNode(node_val, left_tree, right_tree)
        return temp
