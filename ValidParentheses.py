class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            '}': '{',
            ']': '[',
            ')': '(' 
        }
        stack = []
        for char in s:
            # check if it is a closing bracket
            if char in brackets:
                # if no open brackets to close or no match, return invalid
                if not stack or stack[-1] != brackets[char]:
                    return False
                # otheriwse, pop the stack since there is a match
                stack.pop()
            # if it is an opening bracket, add to the stack
            else:
                stack.append(char)
        # if we make it through the entire string, check for any unclosed brackets
        return len(stack) == 0
