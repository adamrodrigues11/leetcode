"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
"""

# Solution 1: Use in-order traversal to get sorted list of node values, then find minimum difference
# time: O(n)
# space: O(n)

class Solution(object):

    def traverseInOrder(self, root, node_vals):
        if not root:
            return
        self.traverseInOrder(root.left, node_vals)
        node_vals.append(root.val)
        self.traverseInOrder(root.right, node_vals)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # use in-order traversal to take advantage of the binary tree structure
        node_vals = []
        self.traverseInOrder(root, node_vals)
        differences = [node_vals[i] - node_vals[i - 1] for i in range(1, len(node_vals))]
        return min(differences)
    
