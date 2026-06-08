# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        hl=self.maxheight(root.left)
        hr=self.maxheight(root.right)
        if abs(hl-hr)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxheight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxheight(root.left),self.maxheight(root.right))