def minimize_max_difference(arr, k):
    n = len(arr)
    
    if n == 1:
        return 0
    
    arr.sort()
    
    ans = arr[n-1] - arr[0]
    
    small = arr[0] + k
    large = arr[n-1] - k
    
    if small > large:
        small, large = large, small
    
    for i in range(1, n-1):
        
        subtract = arr[i] - k
        add = arr[i] + k
        
        if subtract >= small or add <= large:
            continue
        
        if large - subtract <= add - small:
            small = subtract
        else:
            large = add
    
    return min(ans, large - small)


arr = [1, 5, 8, 10]
k = 2

print(" max difference =", minimize_max_difference(arr, k))
