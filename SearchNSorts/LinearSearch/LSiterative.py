def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1

# Main driver code
if __name__ == "__main__":
    # Define an array
    arr = [12, 34, 54, 2, 23, 67, 89, 1, 7, 19]

    # Ask the user for the number to search
    target = int(input("Enter the number you want to search for: "))

    # Perform linear search
    result = search(arr, target)

    # Output the result
    if result != -1:
        print(f"The number {target} is found at index {result}.")
    else:
        print(f"The number {target} is not found in the array.")