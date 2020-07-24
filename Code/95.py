# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    import functools
    def generateTrees(self, n: int) -> List[TreeNode]:
        # self.cache = {}
        if n < 1:
            return []
        return self._generate(1, n)

    @functools.lru_cache
    def _generate(self, start, end):
        if start > end:
            return []
        # if (start, end) in self.cache:
        #     return self.cache[(start, end)]
        trees = []
        for i in range(start, end + 1):
            left_sub_tree = self._generate(start, i - 1)
            right_sub_tree = self._generate(i + 1, end)
            for left in left_sub_tree:
                for right in right_sub_tree:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    trees.append(root)
        # self.cache[(start, end)] = trees
        return trees
