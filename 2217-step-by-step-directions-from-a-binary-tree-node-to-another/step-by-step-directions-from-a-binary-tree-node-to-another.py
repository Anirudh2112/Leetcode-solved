# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findLCA(node, p, q):
            if not node:
                return None
            if node.val == p or node.val == q:
                return node
            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)
            if left and right:
                return node
            return left if left else right
        
        def findPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if findPath(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(node.right, target, path):
                return True
            path.pop()
            return False
        
        lca = findLCA(root, startValue, destValue)
        
        startPath = []
        findPath(lca, startValue, startPath)
        
        destPath = []
        findPath(lca, destValue, destPath)
        
        return 'U' * len(startPath) + ''.join(destPath)