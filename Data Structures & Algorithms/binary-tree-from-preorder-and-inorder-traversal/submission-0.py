# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #took preorder[0] --> 1
        #check using in order everything left or right is the subtree (left or right)
        # recurse on each half how?
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid+1])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
