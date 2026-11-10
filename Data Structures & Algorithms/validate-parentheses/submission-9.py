class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]":"[", "}":"{", ")": "("}
        stack = []

        for character in s:
            if character in closeToOpen:
                if not stack:
                    return False
                check = stack.pop()
                if check != closeToOpen[character]:
                    return False
                continue
            else:
                stack.append(character)
        return len(stack) == 0
        