class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        worklist = []
        operators = {
            "+":lambda x,y:x+y,
            "-":lambda x,y:x-y,
            "/":lambda x,y:int(x/y),
            "*":lambda x,y:x*y,
        }
        for token in tokens:
            if token in operators:
                y = worklist.pop()
                x = worklist.pop()
                res = operators[token](x,y)
                worklist.append(res)
            else:
                worklist.append(int(token))
        
        return worklist.pop()