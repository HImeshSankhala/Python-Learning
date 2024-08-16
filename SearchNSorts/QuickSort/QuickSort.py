def quickSort(arr):
    # Base case: if the array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot element
        pivot = arr[len(arr) // 2]
        # Partition the array into three parts:
        # less than pivot, equal to pivot, and greater than pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Recursively apply quicksort to the left and right sub-arrays
        return quickSort(left) + middle + quickSort(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
print("Unsorted array:", arr)
sorted_arr = quickSort(arr)
print("Sorted array:", sorted_arr)
