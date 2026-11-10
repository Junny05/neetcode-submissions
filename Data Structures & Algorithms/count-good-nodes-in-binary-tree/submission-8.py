# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [float("-inf")]
        # 1 
        def dfs(root,curr_max):
            if not root:
                return 

            if curr_max <= root.val:
                res.append(root.val)
            dfs(root.left,max(curr_max, root.val))
            dfs(root.right,max(curr_max, root.val))
        dfs(root, root.val)
        print(res)
        return len(res) - 1
        
