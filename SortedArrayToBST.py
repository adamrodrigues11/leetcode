"""
Given a non-empty integer array sorted in ascending order, convert it to a height-balanced binary search tree.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Use dfs (pre-order) recursion to build tree

class Solution(object):

    def sortedArrayToBST(self, nums, root=None):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not root:
            root = TreeNode()
        print_str = "called with nums %s and root %s" %(nums, root.val)
        print(print_str)
        mid = len(nums) // 2
        root.val = nums[mid]
        if nums[:mid]:
            root.left = TreeNode()
            self.sortedArrayToBST(nums[:mid], root.left)
        if nums[mid + 1:]:
            root.right = TreeNode()
            self.sortedArrayToBST(nums[mid + 1:], root.right)
        return root

# Solution 2: A cleaner solution from leetcode that has less cases to consider
# This was my original thinking for base case, and place middle as new root and recurse on left and right subarrays (I just didn't know how to implement it)

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    
