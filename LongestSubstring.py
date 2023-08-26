class Solution():
    def longestSubstring(self, s):
        """
        Return the lenght of the longest substring of s without any repeating characters
        :type s: str
        :rtype: int
        """
        longest = 0
        current = 0
        observed = set()
        for char in s:
            if char in observed:
                current = 0
                observed.clear()
            else:
                current += 1
                if current > longest:
                    longest = current
            observed.add(char)
        return longest
    
assert Solution().longestSubstring('abcabcbb') == 3
assert Solution().longestSubstring('bbbbb') == 1
assert Solution().longestSubstring('pwwkew') == 3
assert Solution().longestSubstring('') == 0
