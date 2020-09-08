# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # res = list()
        # self.recursive_sol(root, res)
        # return res
        # return self.iterative_sol(root)
        return self.morris_travel(root)

    def recursive_sol(self, root, res):
        if root:
            self.recursive_sol(root.left, res)
            res.append(root.val)
            self.recursive_sol(root.right, res)

    def iterative_sol(self, root):
        res = list()
        stack = list()
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            temp = stack.pop()
            res.append(root.val)
            root = temp.right
        return res

    def morris_travel(self, root):
        current = root
        res = list()
        while current:
            if not current.left:
                res.append(current.val)
                current = current.right
            else:
                left_child = current.left
                while left_child.right:
                    left_child = left_child.right
                left_child.right = current
                temp = current
                current = current.left
                temp.left = None
        return res
