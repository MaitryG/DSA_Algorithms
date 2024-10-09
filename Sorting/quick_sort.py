def quicksort(arr, left, right):
    if left < right:
        p = get_partition(arr, left, right)
        quicksort(arr, left, p-1)
        quicksort(arr, p+1, right)
    return arr

def get_partition(arr, left, right):
    p = right
    j = -1
    for i in range(left, right):
        if arr[i] < arr[p]:
            j+=1
            swap(arr, i, j)

    j+=1
    swap(arr, j, p)
    return j        
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

print(quicksort([4,34,23,5432,34], 0, 4))