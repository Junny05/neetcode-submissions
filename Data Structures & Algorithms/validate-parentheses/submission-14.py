class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}": "{", "]" : "[", ")" : "("}
        stack = []

        for bracket in s:
            if stack and bracket in closeToOpen:
                check = stack.pop()
                if check != closeToOpen[bracket]:
                    return False
                else:
                    continue
            else:
                stack.append(bracket)
        return len(stack) == 0

            