class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        k = len(nums)
        while i < k - 1:
            if nums[i] == val:                
                nums[i: -1] = nums[i + 1:]
                # nums[-1] = val
                k -= 1
            else:
                i += 1
        if k!= 0 and nums[i] == val:
            k -= 1
        return k

# a cleaner solution
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for x in nums:
            if(x != val):
                nums[count] = x
                count = count + 1
        return count


