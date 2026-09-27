class Solution(object):
    def reverseParentheses(self, s):
        stk = []
        for c in s:
            if c == ")":
                t = []
                while stk and stk[-1] != "(":
                    t.append(stk.pop())
                if stk and stk[-1] == "(":
                    stk.pop()
                stk.extend(t)
            else:
                stk.append(c)
        return "".join(stk)