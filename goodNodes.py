from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, maxVal):
            if not root: return 0
            res = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)
            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)

            return res
        
        return dfs(root, root.val)
    
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
result = solution.goodNodes(tree)
print(result)  