# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle the rows
while row < size:
    # Use a for loop to print asterisks for each column
    for col in range(size):
        print("*", end="")

    # Move to the next line after finishing a row
    print()

    # Increment the row counter
    row += 1
