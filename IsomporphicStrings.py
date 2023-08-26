class Solution():
    def isIsomorphic(self, s, t):
        """
        Determine is s and t are isomorphic strings; that is, the characters in s can be replaced to get t
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        i = 0
        s_to_t = {}
        while i < len(s):
            if s[i] not in s_to_t:
                s_to_t[s[i]] = t[i]
            elif s_to_t[s[i]] != t[i]: return False
            i += 1
        return True

assert Solution().isIsomorphic("egg", "add") == True
assert Solution().isIsomorphic("foo", "bar") == False
assert Solution().isIsomorphic("paper", "title") == True
assert Solution().isIsomorphic("papers", "title") == False

