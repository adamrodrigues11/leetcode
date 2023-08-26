class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kth_smallest(self, root, k, out=None):
        """
        Given the root of a BST, return the kth smallest value of the all the nodes in tree
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # assumed k is less than or equal to the number of nodes in the tree
        # use dfs (pre-order) to add node values in ascending order to a list, stop at the kth value
        if not root:
            return
        if out is None:
            out = []
        if self.kth_smallest(root.left, k, out): return out[-1]
        out.append(root.val)
        if len(out) == k:
            return out[-1]
        if self.kth_smallest(root.right, k, out): return out[-1]

tree1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
tree2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
tree3 = TreeNode(30, TreeNode(10, None, TreeNode(20)), TreeNode(40))

assert Solution().kth_smallest(tree1, 1) == 1
assert Solution().kth_smallest(tree1, 2) == 2
assert Solution().kth_smallest(tree2, 3) == 3
assert Solution().kth_smallest(tree3, 3) == 30

        
