# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(proot, qroot):
            if (not proot and qroot) or (proot and not qroot):
                return False
            
            if (not proot and not qroot):
                return True

            if proot.val != qroot.val:
                return False
        
            left, right = dfs(proot.left,qroot.left), dfs(proot.right,qroot.right)

            return left and right
        
        return dfs(p,q)

            