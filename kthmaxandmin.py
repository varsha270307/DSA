arr = [7, 10, 4, 3, 20, 15]
k = 3

arr.sort()

kth_min = arr[k-1]
kth_max = arr[-k]

print("Kth Minimum =", kth_min)
print("Kth Maximum =", kth_max)
