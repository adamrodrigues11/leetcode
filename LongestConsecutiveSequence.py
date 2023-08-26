class Solution:
    def longestConsecutiveSeq(self, nums):
        """
        Returns the length of the longest consecutive elements sequence in an array of integers, nums.
        :type nums: int[]
        :rtype: int
        """
        # num_set = set()
        # min_num = nums[0]
        # for num in nums[1:]:
        #     if num not in num_set:
        #         num_set.add(num)
        #     if num < min_num:
        #         min_num = num
        num_set = set(nums)
        longest = 0
        while num_set:
            num = num_set.pop()
            current = 1
            while (num + 1) in num_set:
                num += 1
                num_set.remove(num)
                current += 1
            while(num - 1) in num_set:
                num -= 1
                num_set.remove(num)
                current += 1
            if current > longest:
                longest = current
        return longest

assert Solution().longestConsecutiveSeq([]) == 0
assert Solution().longestConsecutiveSeq([1]) == 1
assert Solution().longestConsecutiveSeq([100, 4, 200, 1, 3, 2]) == 4
assert Solution().longestConsecutiveSeq([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

