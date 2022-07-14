def solve():
    s = "anagram"
    t = "nagaram"
    if len(s) != len(t):
        return False

    first_string_map = dict()
    second_string_map = dict()

    for i in range(len(s)):
        first_string_map[s[i]] = 1 + first_string_map.get(s[i], 0)
        second_string_map[t[i]] = 1 + second_string_map.get(t[i], 0)

    for key in first_string_map.keys():
        if first_string_map.get(key, 0) != second_string_map.get(key, 0):
            return False

    return True


print(solve())
