def merge(arr1, arr2, m, n):
    i, j = m - 1, 0

    while i >= 0 and j < n:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1

    arr1.sort()
    arr2.sort()

# Test Case 1
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merge(arr1, arr2, len(arr1), len(arr2))
print("Test Case 1:")
print("arr1:", arr1)
print("arr2:", arr2)

# Test Case 2
arr1 = [10, 12, 14]
arr2 = [1, 3, 5]
merge(arr1, arr2, len(arr1), len(arr2))
print("\nTest Case 2:")
print("arr1:", arr1)
print("arr2:", arr2)

# Test Case 3
arr1 = [2, 3, 8]
arr2 = [4, 6, 10]
merge(arr1, arr2, len(arr1), len(arr2))
print("\nTest Case 3:")
print("arr1:", arr1)
print("arr2:", arr2)

# Test Case 4
arr1 = [1]
arr2 = [2]
merge(arr1, arr2, len(arr1), len(arr2))
print("\nTest Case 4:")
print("arr1:", arr1)
print("arr2:", arr2)

# Test Case 5
arr1 = list(range(1, 50001))
arr2 = list(range(50001, 100001))
merge(arr1, arr2, len(arr1), len(arr2))
print("\nTest Case 5:")
print("arr1:", arr1[:10], "...")  # Displaying only first 10 elements for brevity
print("arr2:", arr2[:10], "...")
