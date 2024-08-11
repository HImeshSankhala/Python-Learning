| **Method**             | **Pros**                                                                                                                                       | **Cons**                                                                                                                                                                                                                 | **Time Complexity** | **Space Complexity** |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | -------------------- |
| **Iterative Search**   | - Simple and easy to understand. <br>- Efficient in terms of memory usage. <br>- No risk of stack overflow.                                    | - Slightly less elegant and can be more verbose for simple problems.                                                                                                                                                     | O(n)                | O(1)                 |
| **Recursive Search**   | - More elegant and mirrors the mathematical concept. <br>- Concise and easy to implement for those familiar with recursion.                    | - Higher memory usage due to multiple stack frames. <br>- Risk of stack overflow for large arrays. <br>- Slightly slower due to function call overhead.                                                                  | O(n)                | O(n)                 |
| **Regex-Based Search** | - Flexible and powerful; can handle more complex patterns. <br>- Can be used in situations where pattern matching within elements is required. | - More complex to understand and implement. <br>- Less efficient than direct iteration or recursion due to string manipulation and regex overhead. <br>- May not be as performant for large arrays or frequent searches. | O(n)                | O(n)                 |

Time Complexity:

Iterative Search: O(n) because it needs to check each element in the worst case.
Recursive Search: O(n) because it makes a recursive call for each element.
Regex-Based Search: O(n) because it scans through the string representation of the array.
Space Complexity:

Iterative Search: O(1) since it uses a constant amount of extra space (only a few variables).
Recursive Search: O(n) due to the additional space required for the recursive call stack.
Regex-Based Search: O(n) because the entire array is converted into a string, and additional space is required for the regex operation.
