class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return (1 + max(left, right))
        else:
            return 0
