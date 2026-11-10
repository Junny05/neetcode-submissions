class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}" : "{", "]" : "[", ")": "("}
        stack = []
        for c in s:
            if c in closeToOpen:
                if not stack:
                    return False
                check = stack.pop()
                if check == closeToOpen[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0