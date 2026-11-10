class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for i in range(len(tokens)):
            if tokens[i] not in "+/*-":
                stack.append(tokens[i])
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                print(num1, num2)
                if tokens[i] == "+":
                    res = num1 + num2
                elif tokens[i] == "*":
                    res = num1 * num2
                elif tokens[i] == "/":
                    res = int(num2 / num1)
                elif tokens[i] == "-":
                    res = num2 - num1
                stack.append(res)
        return res   