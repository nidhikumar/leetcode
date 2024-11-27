def isValid(s: str):
    stack = []
    charMap = {"]": "[", ")": "(", "}":"{"}
    for c in s:
        if c in charMap:
            if stack and stack[-1] == charMap[c]:
                return True
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


print(isValid("()[]"))