# Get number of rows from user
rows = int(input("Enter the number of rows for the diamond: "))

# Upper half of the diamond (including middle)
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Lower half of the diamond
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
