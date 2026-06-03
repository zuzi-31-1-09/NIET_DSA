from typing import Optional

 #Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case: If the tree is empty, return None
        if not root:
            return None

        # Step2: Swap the left and right children
        root.left, root.right = root.right, root.left

        # Step 3: Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Step 4: Return the inverted tree root
        return root