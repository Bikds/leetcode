
#
# def isValid(s: str) -> bool:
#     search = True
#
#     # while search:
#     #     search, s = find(s)
#     search, newstr = find(s)
#     #print(newstr)
#     return search
#
#     #
#     # if len(s) == 0:
#     #     return True
#     # return False
#
# def find(s: str):
#     openparens = ["(", "{", "["]
#     closedparens = [")", "}", "]"]
#     openidx = openparens.index(s[0])
#     closed = closedparens[openidx] in s
#     if closed == False:
#         return (False, s)
#     else:
#         idx_remove = s.index(closedparens[openidx])
#         new_str = s[1:idx_remove] + s[idx_remove+1:]
#         return (True, new_str)

# def isValid(s: str) -> bool:
#     if len(s) == 0:
#         return True
#
#     open_bracket = ["(", "{", "["]
#     closed_bracket = [")", "}", "]"]
#     bracket_idx = open_bracket.index(s[0])
#
#     if closed_bracket[bracket_idx] not in s:
#         return False
#     else:
#         idx_remove = s.index(closed_bracket[bracket_idx])
#         return isValid(s[1:idx_remove])
#     return isValid(s[idx_remove+1])

def isValid(s: str) -> bool:
    if len(s) == 0:
        return True

    open_bracket = ["(", "{", "["]
    closed_bracket = [")", "}", "]"]

    stack = []

    for c in s:
        if c in open_bracket:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            expected_open_bracket = stack.pop()
            if expected_open_bracket != open_bracket[closed_bracket.index(c)]:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(isValid("["))
print(isValid("]"))
print(isValid("()"))
print(isValid("(){}[]"))
print(isValid("(){)"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{()}"))