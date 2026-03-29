# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res_1 = []
        res_2 = []
        def dfs(root,res):
            if not root:
                res.append(root)
                return None
            res.append(root.val)
            left = dfs(root.left,res)
            right = dfs(root.right,res)
        
        dfs(p,res_1)
        dfs(q,res_2)
        if res_1 != res_2:
            return False

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.found = False
        def dfs(r,sub):
            if self.found:
                return
            if not r or not sub:               
                return
            print(r.val)
            print(sub.val)
            if r.val == sub.val:
                self.found = self.isSameTree(r,sub)
            
            left = dfs(r.left,sub)
            right = dfs(r.right,sub)
        dfs(root,subRoot)

        
        return self.found