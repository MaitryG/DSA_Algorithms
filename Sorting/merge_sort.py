def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    # print(mid)
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])

    return merge(left, right)

def merge(arr1, arr2):
    i = 0
    j = 0
    k = 0
    combined = []
    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            combined.append(arr1[i])
            k+=1
            i+=1
        elif arr1[i] >= arr2[j]:
            combined.append(arr2[j])
            j+=1
            k+=1

    if i < len(arr1):
        while i < len(arr1):
            combined.append(arr1[i])
            i+=1
            k+=1

    if j < len(arr2):
        while j < len(arr2):
            combined.append(arr2[j])
            j+=1
            k+=1


    return combined

print(merge_sort([3,4,2,1,34,3]))