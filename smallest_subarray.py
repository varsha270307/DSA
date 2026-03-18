def smallest_subarray(arr, x):
    n = len(arr)
    min_len = n + 1
    
    curr_sum = 0
    start = 0
    
    for end in range(n):
        curr_sum += arr[end]
        
        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1
    
    if min_len == n + 1:
        return 0  
    return min_len

arr = [1, 4, 45, 6, 0, 19]
x = 51

print(smallest_subarray(arr, x))