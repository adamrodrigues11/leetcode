# Space Complexity: O(1)
# Time Complexity: O(n)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            temp_i = s[i]
            if not temp_i.isalnum():
                i += 1
                continue
            temp_j = s[j]
            if not temp_j.isalnum():
                j -= 1
                continue
            if temp_i.lower() != temp_j.lower():
                return False
            else:
                i += 1
                j -= 1
        return True

# alternative solution using list and check if list is equal to its reverse
# uses more space, but is more concise
# space: O(n)
# time: O(n)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lower_chars = [c.lower() for c in s if c.isalnum()]
        return lower_chars == lower_chars[::-1]