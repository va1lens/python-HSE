"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/1484969472/
?envType=problem-list-v2&envId=binary-tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root, ans):
        if not root:
            return
        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)

    def kthSmallest(self, root, k):
        ans = []
        self.inorder(root, ans)
        return ans[k - 1]
