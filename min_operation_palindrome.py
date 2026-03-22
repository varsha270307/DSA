# mpal.py

def min_operations(arr):
    i = 0
    j = len(arr) - 1
    ops = 0

    while i < j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1

        elif arr[i] < arr[j]:
            arr[i + 1] += arr[i]
            i += 1
            ops += 1

        else:
            arr[j - 1] += arr[j]
            j -= 1
            ops += 1

    return ops



arr = [1, 4, 5, 1]
print(min_operations(arr))