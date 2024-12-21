"""
https://leetcode.com/problems/validate-binary-search-tree/submissions/1484924883/
?envType=problem-list-v2&envId=binary-tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minimum, maximum):
            if not node:
                return True
            if not (node.val < maximum and node.val > minimum):
                return False
            return valid(node.left, minimum, node.val) and valid(
                node.right, node.val, maximum
            )

        return valid(root, float("-inf"), float("inf"))
