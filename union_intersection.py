arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]

i = j = 0
union = []
inter = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        union.append(arr1[i])
        i += 1
    elif arr1[i] > arr2[j]:
        union.append(arr2[j])
        j += 1
    else:
        union.append(arr1[i])
        inter.append(arr1[i])
        i += 1
        j += 1

union += arr1[i:]
union += arr2[j:]

print("Union =", union)
print("Intersection =", inter)
