def elements_more_than_n_by_k(arr, k):
    n = len(arr)
    freq = {}

  
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

   
    for key, count in freq.items():
        if count > n // k:
            print(key, end=" ")



arr = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4

elements_more_than_n_by_k(arr, k)