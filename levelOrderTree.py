from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, p: TreeNode):
        res = []
        q = deque()
        q.append(p)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
    
if __name__ == "__main__":
    # Tree 1
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    tree.left.left.left = TreeNode(8)
    tree.left.left.right = TreeNode(9)


    solution = Solution()
    result = solution.levelOrder(tree)

    print("Level order = ", result)