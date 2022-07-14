def solve():
    s = "a"
    t = "ab"
    if len(s) != len(t):
        return False

    first_string_map = dict()
    second_string_map = dict()
    for char in s:
        if char not in first_string_map.keys():
            first_string_map[char] = 1
        else:
            first_string_map[char] += 1

    for char in t:
        if char not in second_string_map.keys():
            second_string_map[char] = 1
        else:
            second_string_map[char] += 1

    for key in first_string_map.keys():
        try:
            if first_string_map[key] != second_string_map[key]:
                return False
        except KeyError:
            return False
    return True


print(solve())
