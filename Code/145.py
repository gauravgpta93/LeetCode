# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.recursive_sol(root, list())
        return self.iterative_sol(root)

    def recursive_sol(self, root, res):
        if not root:
            return res
        self.recursive_sol(root.left, res)
        self.recursive_sol(root.right, res)
        res.append(root.val)
        return res

    def iterative_sol(self, root):
        res = list()
        stack = [root]
        visited = set()
        while stack:
            current = stack.pop()
            if current:
                if current in visited:
                    res.append(current.val)
                else:
                    visited.add(current)
                    stack.append(current)
                    stack.append(current.right)
                    stack.append(current.left)

        return res
