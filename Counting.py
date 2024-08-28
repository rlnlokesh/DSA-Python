def countingSort(arr):
    # Find the maximum element in the array
    max_element = max(arr)

    # Initialize count array with zeros
    count = [0] * (max_element + 1)

    # Count the occurrences of each element
    for num in arr:
        count[num] += 1

    # Update count array to store the actual position of each element
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Initialize the output array
    output = [0] * len(arr)

    # Fill the output array with sorted elements
    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1

    return output


# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = countingSort(arr)
print("Sorted array is:", sorted_arr)
