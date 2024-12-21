"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/1484939664/
?envType=problem-list-v2&envId=binary-tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []

        def dfs(node, level, res):
            if not node:
                return
            if len(res) <= level:
                res.append([])
            dfs(node.left, level + 1, res)
            dfs(node.right, level + 1, res)
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)

        dfs(root, 0, res)
        return res
