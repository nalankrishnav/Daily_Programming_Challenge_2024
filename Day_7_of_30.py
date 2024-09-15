from collections import defaultdict

def water_height(arr):
    a=defaultdict(list)
    maxi=0
    for i in range(len(arr)-2):
        if arr[maxi]<arr[i]:
            maxi=i
        a[i+1].append(maxi)
    maxii=len(arr)-1
    for i in range(len(arr)-1,1,-1):
        if arr[maxii]<arr[i]:
            maxii=i
        a[i-1].append(maxii)
    sum=0
    for i in a:
        k=min(arr[a[i][0]],arr[a[i][1]])
        
        if arr[i]<k:
            sum+=(k-arr[i])
            
    return sum
print(water_height([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(water_height([4, 2, 0, 3, 2, 5]))
print(water_height( [1, 1, 1]))
print(water_height([5]))
print(water_height([2, 0, 2]))


