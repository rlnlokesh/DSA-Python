# def binary_search(arr, target):
#
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         # Check if target is present at mid
#         if arr[mid] == target:
#             return mid
#
#         # If target is greater, ignore left half
#         elif arr[mid] < target:
#             left = mid + 1
#
#         # If target is smaller, ignore right half
#         else:
#             right = mid - 1
#
#     # If target is not found in the array
#     return -1
#
# # Example usage:
# arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# target = 9
# result = binary_search(arr, target)
# if result != -1:
#     print(f"Target {target} found at index {result}.")
# else:
#     print(f"Target {target} not found in the array.")
#

def binary_search(arr,target):
     left = 0
     right = len(arr)-1

     while(left <= right):
         mid = (left+right)//2
         if arr[mid] == target:
             return mid
         if arr[mid] < left:
             left = mid + 1
         if arr[mid] > right:
             right = mid - 1


     return -1

array = [1,2,3,4,5,6,7,8]
a = binary_search(array,4)
print("address of ",4,"is",a)



