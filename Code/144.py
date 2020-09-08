# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.recursive_call(root, [])
        # return self.iterative_call(root)
        return self.morris_travel(root)

    def recursive_call(self, root, res):
        if not root:
            return res
        res.append(root.val)
        self.recursive_call(root.left, res)
        self.recursive_call(root.right, res)
        return res

    def iterative_call(self, root):
        res = list()
        stack = [root] if root else []
        current = 0
        while current < len(stack):
            temp = stack.pop()
            res.append(temp.val)
            stack.append(temp.right) if temp.right else None
            stack.append(temp.left) if temp.left else None
        return res

    def morris_travel(self, root):
        res = list()
        current = root
        while current:
            res.append(current.val)
            if not current.left:
                current = current.right
            else:
                temp = current.left
                while temp.right:
                    temp = temp.right
                temp.right = current.right
                current = current.left
        return res