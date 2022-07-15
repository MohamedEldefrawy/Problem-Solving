def solution():
    s = "race a car"
    if ''.join(filter(str.isalnum, s)).lower() == ''.join(filter(str.isalnum, s)).lower()[::-1]:
        return True
    return False


print(solution())
