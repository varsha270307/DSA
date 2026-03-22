# twp.py

def three_way_partition(arr, x):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < x:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == x:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


arr = [2, 1, 5, 6, 3, 4, 5]
x = 5
print(three_way_partition(arr, x))