 #Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val 
         self.left = left
         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case: If the node is empty , depth is 0
        if not root:
            return 0

        # Recursive Step: Get the depth of both sides
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Take the maximum of the two depths and add 1 for the current node
        return max(left_depth, right_depth) + 1
    