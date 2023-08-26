# Remove duplicates from sorted array in place, return the number of unique elements
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums[1:]:
            if nums[i] != num:
                i += 1
                nums[i] = num
        return i + 1

# Follow up: allow at most 2 duplicates, return the length of the "cleaned" portion of the array
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        counter = 1
        for num in nums[1:]:
            if nums[i] != num:
                counter = 1
            else:
                counter += 1
            if counter <= 2:
                i += 1
                nums[i] = num
        return i + 1
            