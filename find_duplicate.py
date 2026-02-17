def find_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)

arr = [1, 3, 4, 2, 2]
print("Duplicate element is:", find_duplicate(arr))
