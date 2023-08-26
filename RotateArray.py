class Solution():
    def rotateArray(self, nums, k):
        """
        :type nums: int[]
        :type k: int
        :rtype: int[]
        """
        shift = k % len(nums)
        if shift != 0:
            temp = nums[:-1 * shift]
            nums[:shift] = nums[-1 * shift:]
            nums[shift:] = temp
        return nums
    
assert Solution().rotateArray([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
assert Solution().rotateArray([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
assert Solution().rotateArray([-1, -100, 3, 99], 4) == [-1, -100, 3, 99]
assert Solution().rotateArray([5], 6) == [5]
