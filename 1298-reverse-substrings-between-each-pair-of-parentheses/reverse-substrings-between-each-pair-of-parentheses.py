class Solution(object):
    def reverseParentheses(self, s):
        stk = []
        for c in s:
            if c == ")":
               
