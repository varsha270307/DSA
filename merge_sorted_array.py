import math

def nextGap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)

def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    gap = nextGap(n + m)

    while gap > 0:
        i = 0
        j = gap

        while j < (n + m):
            

            if i < n and j < n:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            elif i < n and j >= n:
                if arr1[i] > arr2[j - n]:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]
            else:
                if arr2[i - n] > arr2[j - n]:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]

            i += 1
            j += 1

        gap = nextGap(gap)


arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]

merge(arr1, arr2)

print("Merged arrays:")
print(arr1)
print(arr2)
