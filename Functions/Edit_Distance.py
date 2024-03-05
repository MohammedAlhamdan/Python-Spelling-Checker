def editDistance(str1, str2):
    # Get the lengths of the input strings
    m = len(str1)
    n = len(str2)
     
    # Initialize a list to store the current row
    current = [0] * (n + 1)
     
    # Initialize the first row with values from 0 to n
    for j in range(n + 1):
        current[j] = j
     
    # Initialize a variable to store the previous value
    previous = 0
     
    # Loop through the rows of the dynamic programming matrix
    for i in range(1, m + 1):
        # Store the current value at the beginning of the row
        previous = current[0]
        current[0] = i
         
        # Loop through the columns of the dynamic programming matrix
        for j in range(1, n + 1):
            # Store the current value in a temporary variable
            temp = current[j]
             
            # Check if the characters at the current positions in str1 and str2 are the same
            if str1[i - 1] == str2[j - 1]:
                current[j] = previous
            else:
                # Update the current cell with the minimum of the three adjacent cells
                current[j] = 1 + min(previous, current[j - 1], current[j])
             
            # Update the previous variable with the temporary value
            previous = temp
     
    # The value in the last cell represents the minimum number of operations
    return current[n]
 

str1 = "night"
str2 = "nigt"   
ans = editDistance(str1, str2)
print(ans)