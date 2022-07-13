def sol():
    # nums = [2, 14, 18, 22, 22]
    nums = [1, 2, 3, 4]
    numbers_dict = set()
    for number in nums:
        if number in numbers_dict:
            return True
        numbers_dict.add(number)
    return False


print(sol())
