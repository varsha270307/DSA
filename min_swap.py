# msk.py

def min_swaps(arr, k):
    n = len(arr)

    # Step 1: count elements <= k
    count = 0
    for i in arr:
        if i <= k:
            count += 1

    # Step 2: count bad elements in first window
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1

    ans = bad

    # Step 3: slide window
    i = 0
    j = count

    while j < n:
        # remove left element
        if arr[i] > k:
            bad -= 1

        # add right element
        if arr[j] > k:
            bad += 1

        ans = min(ans, bad)

        i += 1
        j += 1

    return ans



arr = [2, 1, 5, 6, 3]
k = 3
print(min_swaps(arr, k))