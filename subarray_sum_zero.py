
def subArrayExists(arr):
    s = set()
    curr_sum = 0

    for i in arr:
        curr_sum += i

        
        if curr_sum == 0 or curr_sum in s:
            return True

        s.add(curr_sum)

    return False


arr = [4, 2, -3, 1, 6]

if subArrayExists(arr):
    print("Subarray with sum 0 exists")
else:
    print("No subarray with sum 0 exists")