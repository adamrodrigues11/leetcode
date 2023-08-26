class Solution():
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if the test sequence is empty, it is by definition a subsequence
        if not s:
            return True
        # if the test sequence is non-empty and the main sequence is empty, the test sequence is not a sub-sequence
        if not t:
            return False
        # if both are non-empty, we can use two pointers
        i = 0
        j = 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                if i == len(s): return True
            j += 1
        return False

assert Solution().isSubsequence("", "") == True
assert Solution().isSubsequence("", "dfgdg") == True
assert Solution().isSubsequence("a", "") == False
assert Solution().isSubsequence("abc", "ahbgdc") == True
assert Solution().isSubsequence("axc", "ahbgdc") == False
assert Solution().isSubsequence("abcd", "abc") == False
