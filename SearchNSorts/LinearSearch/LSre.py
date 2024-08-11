import re

def search(arr, x):
    # Convert the array to a string
    arr_str = ','.join(str(i) for i in arr)

    # Use regular expression to search for the element in the string
    match = re.search(r'\b{}\b'.format(x), arr_str)

    # Output
    if match:
        # Calculate the index by counting the number of commas before the match
        result = arr_str[:match.start()].count(',')
        return result
    else:
        return -1

# Main driver code
if __name__ == "__main__":
    # Define an array
    arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

    # Ask the user for the number to search
    target = int(input("Enter the number you want to search for: "))

    # Perform search using regular expression
    result = search(arr, target)

    # Output the result
    if result != -1:
        print(f"Element {target} is present at index {result}.")
    else:
        print(f"Element {target} is not present in the array.")
