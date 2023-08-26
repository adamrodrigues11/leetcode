class Solution:
    def pathSum(self, root, targetSum, pathSum=0):
        """
        Given the root of a binary tree and an int targetSum, 
        determine if the tree has a root-to-leaf path with sum equal to the target.
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool 
        """
        # if empty tree, return False
        if not root:
            return False
        # add current value to pathSum
        pathSum += root.val
        # base case: node is a leaf
        if not (root.left or root.right):
            if pathSum == targetSum:
                return True
            else:  # remove leaf from pathSum as we go up to parent
                pathSum -= root.val
                return False   
        # traverse per-order
        return self.pathSum(root.left, targetSum, pathSum) or self.pathSum(root.right, targetSum, pathSum)
        

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = TreeNode(1, TreeNode(2), TreeNode(3))

new_tree = TreeNode(5, 
                    TreeNode(4, 
                            TreeNode(11, 
                                    TreeNode(7), 
                                    TreeNode(2)
                            )
                    ),
                    TreeNode(8,
                            TreeNode(13),
                            TreeNode(4, 
                                    None, 
                                    TreeNode(1)
                            )
                    )
            )

assert Solution().pathSum(tree, 5) == False
assert Solution().pathSum(tree, 4) == True

assert Solution().pathSum(new_tree, 22) == True
assert Solution().pathSum(new_tree, -10) == False