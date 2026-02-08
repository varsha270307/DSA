arr = [1, -2, 3, -4, -1, 6, -7, 8]

j = 0
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

print(arr)
