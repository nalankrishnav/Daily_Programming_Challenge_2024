from collections import defaultdict

def sum_of_subarray(arr):
    sum = 0
    dic = defaultdict(list)
    result = []

    dic[0].append(-1)  

    for i in range(len(arr)):
        sum += arr[i]

        if sum in dic:
            for start in dic[sum]:
                result.append((start + 1, i))

        dic[sum].append(i)

    return result

print(sum_of_subarray([4, -1, -3, 1, 2, -1]))
print(sum_of_subarray([1, 2, 3, 4]))
print(sum_of_subarray([0, 0, 0]))
print(sum_of_subarray([-3, 1, 2, -3, 4, 0]))
print(sum_of_subarray([1, 2, -3, 3, -1, 2]*10000))
