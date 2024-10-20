class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expression = "|(" + expression + ")"
        oper = []
        stack = []

        for char in expression:
            if char in "|&!":
                oper.append(char)
            elif char in "(tf":
                m = {"(":"(","t":True,"f":False}
                stack.append(m[char])
            elif char == ")":
                curr = stack[-1]
                while stack[-1] != "(":
                    item = stack.pop()
                    if oper[-1] == "|": curr = curr or item
                    elif oper[-1] == "&": curr = curr and item
                    else: curr = not item
                
                stack.pop() # should be (
                oper.pop()
                stack.append(curr)
        
        return stack.pop()
