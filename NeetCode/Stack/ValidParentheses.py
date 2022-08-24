# s = "()[]{}"


s = "([)]"


def solution():
    stack = []
    parentheses_map = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    for character in s:
        if character not in parentheses_map:
            stack.append(character)
        else:
            if stack and stack[-1] == parentheses_map[character]:
                stack.pop()
            else:
                return False
    return True if not stack else False


print(solution())
