class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}":"{", "]":"[", ")":"("}
        stack = []

        for item in s:
            if item in closeToOpen:
                if not stack or stack.pop() != closeToOpen[item]:
                    return False
            else:
                stack.append(item)
        return len(stack) == 0

