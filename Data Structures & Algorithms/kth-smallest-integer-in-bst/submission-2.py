# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 2 (1st path) -> 1 (2nd path)  2 != 1 if k == 1 
        # 2 -> 3

        # 1 3
        arr = []
        def dfs(root):
            if not root:
                return 

            dfs(root.left)
            arr.append(root.val)           
            dfs(root.right)
        dfs(root)
        arr.sort()
        print(arr)
        return arr[k-1]

            
