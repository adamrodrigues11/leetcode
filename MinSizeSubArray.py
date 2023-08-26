# Find the size of the smallest contiguous subarray whose sum is greater than or equal to ‘target’.
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = len(nums) + 1
        back = 0
        front = 0
        sub_sum = nums[front]
        while back < len(nums):
            if sub_sum >= target:
                min_length = min(min_length, front - back + 1)
                sub_sum -= nums[back]
                back += 1
            else:
                if front < len(nums) - 1:
                    front += 1
                    sub_sum += nums[front]
                else:
                    break
        if min_length <= len(nums):
            return min_length
        else:
            return 0

# A better solution, following my initial idea
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = len(nums) + 1
        back = 0
        window_sum = 0
        for front in range(len(nums)):
            window_sum += nums[front]
            while window_sum >= target:
                min_length = min(min_length, front - back + 1)
                window_sum -= nums[back]
                back += 1
        return 0 if min_length > len(nums) else min_length