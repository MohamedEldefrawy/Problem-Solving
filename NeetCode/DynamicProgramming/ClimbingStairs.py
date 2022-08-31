n = 5
first = 1
second = 1
i = 0
while i in range(n-1):
    temp = first
    first += second
    second = temp
    i +=1
print(first)