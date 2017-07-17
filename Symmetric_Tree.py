# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subSymmetric(self, left, right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        if left.val!=right.val:
            return False
        return self.subSymmetric(left.left, right.right) and self.subSymmetric(left.right, right.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        else:
            return self.subSymmetric(root.left, root.right)
