"""Valid parentheses, Leetcode no. 20"""

class Solution(object):
    def isValid(self, string: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        table = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for char in string:
            if not char in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        if len(stack) > 0:
            return False

        return True
