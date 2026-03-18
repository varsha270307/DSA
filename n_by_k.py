def more_than_n_by_k(arr, k):
    n = len(arr)
    candidates = {}
    
    # Step 1: Find potential candidates
    for num in arr:
        if num in candidates:
            candidates[num] += 1
        elif len(candidates) < k - 1:
            candidates[num] = 1
        else:
            remove = []
            for key in candidates:
                candidates[key] -= 1
                if candidates[key] == 0:
                    remove.append(key)
            for key in remove:
                del candidates[key]
    
    
    result = []
    for key in candidates:
        if arr.count(key) > n // k:
            result.append(key)
    
    return result



arr = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4

print(more_than_n_by_k(arr, k))