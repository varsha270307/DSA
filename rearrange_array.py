def rearrange(arr):
    n = len(arr)
    
    
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    
    pos = i + 1     
    neg = 0         

    while pos < n and neg < pos and arr[neg] < 0:
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2

arr = [1, 2, 3, -4, -1, 4]
rearrange(arr)
print(arr)