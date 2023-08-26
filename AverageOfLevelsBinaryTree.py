"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
"""

# Solution 1: Use breadth-first search to get average at each step (queue)
# time: O(n)
# space: O(n)

from collections import deque

class Solution(object):
     def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # apply BFS pattern and get average at each step
        queue = deque([root])
        averages = []
        while queue:
            level_sum = 0
            level_count = len(queue)
            for _ in range(level_count):
                current = queue.popleft()
                level_sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            averages.append(level_sum / float(level_count))
        return averages

# can also do this using a temp queue for children and swapping at each level
class Solution(object):
     def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # apply BFS pattern and get average at each step
        queue = deque([root])
        averages = []
        while queue:
            level_sum = 0
            level_count = 0
            temp = deque([])
            while queue:
                current = queue.popleft()
                level_sum += current.val
                level_count += 1
                if current.left:
                    temp.append(current.left)
                if current.right:
                    temp.append(current.right)
            averages.append(level_sum / float(level_count))
            queue = temp
        return averages


# Solution 2: Use dfs (pre-order) recursion and store values by height in a dictionary which we will use to calculate averages
# time: O(n*log(n)), log(n) for dictionary lookup/store worst case 
# space: O(h) (h is height of tree, worst case is O(n) if tree is linear)

class Solution(object):
    # populate an output dictionary of values by height as we traverse pre-order
    def groupByHeight(self, root, values_by_level, h=0):
            if not root:
                return
            if h in values_by_level:
                values_by_level[h].append(root.val)
            else:
                values_by_level[h] = [root.val]
            self.groupByHeight(root.left, values_by_level, h + 1)
            self.groupByHeight(root.right, values_by_level, h + 1)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        values_by_level = {}
        self.groupByHeight(root, values_by_level)
        return [sum(values_by_level[h]) / float(len(values_by_level[h])) for h in values_by_level]