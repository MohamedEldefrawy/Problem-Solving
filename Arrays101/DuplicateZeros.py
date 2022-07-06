arr = [1, 0, 2, 3, 0, 4, 5, 0]

index = 0
while index < len(arr) - 1:
    if arr[index] == 0:
        outer_temp = arr[index + 1]
        arr[index + 1] = 0
        j = index + 2
        while j < len(arr):
            temp = arr[j]
            arr[j] = outer_temp
            outer_temp = temp
            j += 1
        index += 2
    else:
        index += 1
print(arr)
