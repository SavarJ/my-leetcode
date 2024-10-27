class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        keep = {} #chars we will keep
        stack = []
        for i, c in enumerate(s):
            if c.isalpha():
                keep[i] = c
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack and s[stack[-1]] == "(":
                    j = stack.pop()
                    keep[i] = ")"
                    keep[j] = "("
        
        return ''.join(keep[i] for i in range(len(s)) if i in keep)
