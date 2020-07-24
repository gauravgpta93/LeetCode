# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = list()
        next_level = [root]
        while root and next_level:
            ans.append([node.val for node in next_level])
            temp = [(node.left, node.right) for node in next_level]
            next_level = [child for node in temp for child in node if child]
        return ans
