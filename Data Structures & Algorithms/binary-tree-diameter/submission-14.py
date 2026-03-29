# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root):
            if not root:
                return 0
            
            return 1 + max(dfs(root.left),dfs(root.right))
        
        left = dfs(root.left)
        right = dfs(root.right)

        sub = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return max(left+right,sub)