arr = [1, 0, 2, 3, 0, 4, 5, 0]

index = 0
while index < len(arr) - 1:
    if arr[index] == 0:
        arr.insert(index + 1, 0)
        arr.pop(len(arr)-1)
        index += 2
    else:
        index += 1

print(arr)
