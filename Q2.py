def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x<pivot]
        right = [x for x in arr[1:] if x>=pivot]
        return quicksort(left)+[pivot]+quicksort(right)

arr = [2,4,2,5,74,3,72,8,87]
print("Given array is ")
print(arr)
print("Sorted array is ")
print(quicksort(arr))