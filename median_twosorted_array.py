def find_median(arr1, arr2):
    n = len(arr1)
    i = j = 0
    count = 0
    m1 = m2 = -1
    
    
    while count <= n:
        if i == n:
            m1 = m2
            m2 = arr2[0]
            break
        elif j == n:
            m1 = m2
            m2 = arr1[0]
            break
        
        if arr1[i] <= arr2[j]:
            m1 = m2
            m2 = arr1[i]
            i += 1
        else:
            m1 = m2
            m2 = arr2[j]
            j += 1
        
        count += 1
    
    return (m1 + m2) / 2



arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]

print(find_median(arr1, arr2))