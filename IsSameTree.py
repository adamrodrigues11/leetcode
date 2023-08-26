"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

# Solution 1: Use breadth-first search to check equality at each step (queue)
# time: O(n)
# space: O(n)

from collections import deque

class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # apply BFS pattern and check equality at each step
        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue and q_queue:
            current_p = p_queue.popleft()
            current_q = q_queue.popleft()
            # if both are None, skip to next in queue
            if not current_p and not current_q:
                continue
            # this is now XOR because of above guard
            if not current_p or not current_q:
                return False
            # only case remaining is both are not None
            # check equality as condition to continue
            if current_p.val != current_q.val:
                return False
            # continue by adding all children to the queue
            p_queue.append(current_p.left)
            p_queue.append(current_p.right)
            q_queue.append(current_q.left)
            q_queue.append(current_q.right)
        return True


# Solution 2: Use dfs (pre-order) recursion to check equality at each step
# time: O(n)
# space: O(n) (worst case, if tree is linear)

class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """        
        # base case: if both are None, return True
        if not p and not q:
            return True
        # if one is None and the other is not, return False
        if not p or not q:
            return False
        # if both are not None, check equality
        if p.val != q.val:
            return False
        # if equal, continue by checking children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)