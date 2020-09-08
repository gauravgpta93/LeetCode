# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # return self.compare_rec(root.left, root.right) if root else True
        return self.compare_iterative(root) if root else True

    def compare_rec(self, left, right):
        if not left and not right:
            return True
        elif left and right:
            if left.val == right.val:
                t1 = self.compare_rec(left.left, right.right)
                t2 = self.compare_rec(left.right, right.left)
                return t1 and t2
        else:
            return False

    def compare_iterative(self, root):
        s1, s2 = [root.left], [root.right]
        while s1 and s2:
            t1 = s1.pop()
            t2 = s2.pop()
            if t1 and t2:
                if t1.val != t2.val:
                    return False
                s1 += [t1.right, t1.left]
                s2 += [t2.left, t2.right]
            elif not t1 and not t2:
                continue
            else:
                return False
        return not s1 and not s2
