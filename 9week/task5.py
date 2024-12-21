"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/1484939132/
?envType=problem-list-v2&envId=binary-tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []

        def dfs(node, level):
            if not node:
                return
            if len(res) < level + 1:
                res.append([])
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            res[level].append(node.val)

        dfs(root, 0)
        return res[::-1]
