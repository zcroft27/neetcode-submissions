class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "*", "-", "/"}
        stack = []
        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:
                f_right = stack.pop()
                f_left = stack.pop()
                if tok == "+":
                    res = f_left + f_right
                    stack.append(res)
                if tok == "-":
                    res = f_left - f_right
                    stack.append(res)
                if tok == "*":
                    res = f_left * f_right
                    stack.append(res)
                if tok == "/":
                    res = int(f_left/f_right)
                    stack.append(res)
        return stack.pop()