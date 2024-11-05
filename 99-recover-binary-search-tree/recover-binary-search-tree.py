# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder_traversal(node):
            if not node:
                return

            inorder_traversal(node.left)

            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node

            self.prev = node

            inorder_traversal(node.right)
            
        inorder_traversal(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val
