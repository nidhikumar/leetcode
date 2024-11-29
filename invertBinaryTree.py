from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertBinaryTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root: return 
            tmp = root.left
            root.left = root.right
            root.right = tmp
            dfs(root.left)
            dfs(root.right)

            return root
        
        return dfs(root)
    
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
result = solution.invertBinaryTree(tree)
print(result)  