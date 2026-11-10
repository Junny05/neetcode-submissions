class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                print(num1,num2)
                if tokens[i] == "-":
                    result = int(num2) - int(num1)
                    stack.append(result)
                if tokens[i] == "+":
                    result = int(num1) + int(num2)
                    stack.append(result)
                if tokens[i] == "/":
                    result = int(num2 / num1)
                    stack.append(result)                   
                if tokens[i] == "*":
                    result = int(num1) * int(num2)
                    stack.append(result)
        return stack[-1]

