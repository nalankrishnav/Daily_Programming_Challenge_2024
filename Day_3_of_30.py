def finding_duplicate_no(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    length = len(arr)
    duplicate_no=(length-((length*(length+1)/2)-total_sum))
    print (int(duplicate_no))
    
finding_duplicate_no([1, 3, 4, 2, 2])
finding_duplicate_no([3, 1, 3, 4, 2])
finding_duplicate_no([1, 1])
finding_duplicate_no([1, 4, 4, 2, 3])
list = list(range(1,1000000))
list.append(50000)
finding_duplicate_no(list)