# time: O(n)
# space: O(n)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        ways = [1, 2]
        for k in range(n - 2):
            ways.append(ways[k + 1] + ways[k])
        return ways[-1]

# time: O(n)
# space: O(1)
class Solution(object):
    def ClimbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        ways = [1, 2]
        for k in range(2, n):
            ways[0], ways[1] = ways[1], ways[0] + ways[1]
        return ways[1]


# now using recursion and memoization
class Solution(object):
    def climbStairs(self, n, cache=None):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        if cache == None:
            cache = {}
        if n in cache:
            return cache[n]
        result = self.climbStairs(n - 1, cache) + self.climbStairs(n - 2, cache)
        cache[n] = result
        return result