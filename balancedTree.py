# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return [True,0]

        def dfs(root):
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and (abs(left[1] - right[1])<=1)
            return (balanced, 1+ max(left[1],right[1]))
        
        return dfs(root)[0]
    
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
result = solution.isBalanced(tree)
print(result)  