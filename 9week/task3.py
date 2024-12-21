"""
https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1484930913/
?envType=problem-list-v2&envId=binary-tree
"""

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        d = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            d[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return list(d.values())
