# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def remove_leaves(node: TreeNode) -> TreeNode:
            if not node:
                return None
            
            node.left = remove_leaves(node.left)
            node.right = remove_leaves(node.right)
            
            if not node.left and not node.right and node.val == target:
                return None
            return node
        return remove_leaves(root)
        