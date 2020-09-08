# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import reduce


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = list()
        next_level = [root]
        while root and next_level:
            ans.append([node.val for node in next_level])
            temp = [(node.left, node.right) for node in next_level]
            next_level = [child for node in temp for child in node if child]
        return ans

    def levelOrder_1(self, root: TreeNode) -> List[List[int]]:
        ans = [[root]] if root else [[]]
        current = 0
        while ans[current]:
            temp_list = list(map(lambda x: [x.left, x.right], ans[current]))
            temp_list = list(reduce(lambda x, y: x + y, temp_list))
            temp_list = list(filter(lambda x: True if x else False, temp_list))
            ans.append(temp_list)
            current += 1
        ans = list(map(lambda x: [y.val for y in x], ans))
        return ans[:-1]
