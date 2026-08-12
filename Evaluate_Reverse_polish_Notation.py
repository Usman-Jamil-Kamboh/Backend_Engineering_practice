class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operends = []

        for ch in tokens :
            if ch == "+" or ch == "*" or ch == "-" or ch == "/" :
                op2 = operends.pop()
                op1 = operends.pop()
                match ch:
                    case "+":
                        operends.append(op1 + op2)
                    case "-":
                        operends.append(op1 - op2)
                    case "*":
                        operends.append(op1 * op2)
                    case "/":
                        operends.append(int(op1 / op2))
            else :
                operends.append(int(ch))
        return operends[0]
                
        
