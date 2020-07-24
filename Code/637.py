# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = list()
        node_list = list()
        node_list.append(root)
        while node_list:
            ans.append(sum([node.val for node in node_list]) / len(node_list))
            node_list = [child for node in node_list for child in (node.left, node.right) if child]
        return ans
