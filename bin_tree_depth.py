
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Given a binary tree, find its maximum depth.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findDepth(root)


    def findDepth(self, root):

        if root == None:
            return 0

        ld = 1 + self.findDepth(root.left)

        rd = 1 + self.findDepth(root.right)

        return max([ld, rd])
