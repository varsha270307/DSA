# Binary Search

arr = [2, 4, 6, 8, 10, 12]
target = 8

start = 0
end = len(arr) - 1

found = False

while start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
        print("Element found at index", mid)
        found = True
        break
    elif arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

if not found:
    print("Element not found")