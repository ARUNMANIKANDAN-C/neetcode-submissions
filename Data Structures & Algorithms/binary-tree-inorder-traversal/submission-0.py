class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)      # left
            res.append(node.val) # center
            dfs(node.right)     # right
        
        dfs(root)
        return res