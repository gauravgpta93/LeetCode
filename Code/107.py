# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        import collections
        ans = list()
        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node:
                if level >= len(ans):
                    ans.insert(0, list())
                ans[-(level + 1)].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return ans
