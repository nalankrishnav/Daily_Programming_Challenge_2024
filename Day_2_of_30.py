def miss_array(arr):
    l=len(arr)+1
    sumr=(l*(l+1))//2
    sumf=0
    for i in arr:
        sumf+=i
    return sumr-sumf
#test cases
#Test Case 1
print(miss_array( [1, 2, 4, 5]))
#Test Case 2
print(miss_array([2, 3, 4, 5]))
#Test Case 3
print(miss_array([1, 2, 3, 4]))
#Test Case 4
print(miss_array([1]))
#Test Case 5
print(miss_array(list(range(1, 1000000))))

#time complexity: O(n) where n is the size of the array
#space complexity: O(1)
