def find_triplet(arr, target):
    arr.sort()
    n = len(arr)

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                print("Triplet:", arr[i], arr[left], arr[right])
                return
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    print("No triplet found")



arr = [1, 4, 45, 6, 10, 8]
target = 22

find_triplet(arr, target)