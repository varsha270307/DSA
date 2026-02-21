def find_pairs(arr, target):
    seen = set()
    pairs = set()
    
    for num in arr:
        complement = target - num
        
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        
        seen.add(num)
    
    return list(pairs)


arr = [1, 5, 7, -1, 5]
target = 6
print(find_pairs(arr, target))