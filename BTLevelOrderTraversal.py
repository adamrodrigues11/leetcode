class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def group_by_height(self, root, values_by_level, height=0):
        if not root:
            return
        if height in values_by_level:
            values_by_level[height].append(root.val)
        else:
            values_by_level[height] = [root.val]
        self.group_by_height(root.left, values_by_level, height + 1)
        self.group_by_height(root.right, values_by_level, height + 1)
        
    def levelOrder(self, root):
        """
        :rtype root: TreeNode
        :rtype: List[List[int]]
        """
        values_by_level = {}
        self.group_by_height(root, values_by_level)
        return [values_by_level[h] for h in values_by_level]

tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
tree2 = TreeNode(1)
tree3 = None

assert Solution().levelOrder(tree1) == [[3], [9, 20], [15, 7]]
assert Solution().levelOrder(tree2) == [[1]]
assert Solution().levelOrder(tree3) == []