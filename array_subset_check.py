def is_subset(arr1, arr2):
    s = set(arr1)

    for num in arr2:
        if num not in s:
            return False

    return True



arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

if is_subset(arr1, arr2):
    print("arr2 is a subset of arr1")
else:
    print("arr2 is not a subset of arr1")