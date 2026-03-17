def longest_consecutive_subsequence(arr):
    s = set(arr)
    longest = 0

    for num in s:
        
        if num - 1 not in s:
            current = num
            length = 1

           
            while current + 1 in s:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest



arr = [100, 4, 200, 1, 3, 2]

print("Length of longest consecutive subsequence:",
      longest_consecutive_subsequence(arr))