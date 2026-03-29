# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.result = []
        if not root:
            return True
        if not root.left and not root.right:
            return True
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            print(left)
            print(right)
            print("ppppp")
            self.res = 0 <= left-right <= 1 or 0 <= right-left <= 1
            self.result.append(self.res)
            return 1 + max(left,right)
        dfs(root)
        return self.result.count(False) == 0