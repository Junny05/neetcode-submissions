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

        def dfs(root):
            if not root:
                return 0

            leftH = dfs(root.left)
            rightH = dfs(root.right)
            
            if leftH == -1 or rightH == -1:
                return -1

            if (abs(leftH - rightH) > 1):
                return -1

            return 1 + max(leftH, rightH)

        if dfs(root) == -1:
            return False
        return True
            
