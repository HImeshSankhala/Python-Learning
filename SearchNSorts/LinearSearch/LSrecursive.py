def search(arr, curr_index, key):
    if curr_index == -1:  # Base case: if the index goes out of bounds
        return -1
    if arr[curr_index] == key:  # If the key is found
        return curr_index
    return search(arr, curr_index-1, key)  # Recursive call with the previous index

# Main driver code
if __name__ == "__main__":
    # Define an array
    arr = [12, 34, 54, 2, 23, 67, 89, 1, 7, 19]

    # Ask the user for the number to search
    target = int(input("Enter the number you want to search for: "))

    # Perform linear search from the last index
    result = search(arr, len(arr) - 1, target)

    # Output the result
    if result != -1:
        print(f"The number {target} is found at index {result}.")
    else:
        print(f"The number {target} is not found in the array.")
