def sort_array_012(arr):
    a1=a2=a3=0
    for i in arr:
        if i==0:
            a1+=1
        elif i==1:
            a2+=1
        elif i==2:
            a3+=1
    j=0
    for i in range(a1):
        arr[j]=0
        j+=1
    for i in range(a2):
        arr[j]=1
        j+=1
    for i in range(a3):
        arr[j]=2
        j+=1
    return arr
a= [0, 1, 2, 1, 0, 2, 1, 0]
print(sort_array_012(a))
a=  [2, 2, 2, 2]
print(sort_array_012(a))
a= [0, 0, 0, 0]
print(sort_array_012(a))
a=  [1, 1, 1, 1]
print(sort_array_012(a))
a= [2, 0, 1]
print(sort_array_012(a))
a= []
print(sort_array_012(a))
