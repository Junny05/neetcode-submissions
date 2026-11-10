class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}": "{", "]" : "[", ")" : "("}
        stack = []

        for bracket in s:
            if bracket in closeToOpen: 
                if not stack or stack.pop() != closeToOpen[bracket]:
                    return False
            else: 
                stack.append(bracket)
        return len(stack) == 0

            