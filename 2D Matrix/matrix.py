rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns:"))

matrix = []
for i in range(rows):
    row = list(map(int,input(f"Enter the elements of row {i+1}: ").split()))
    matrix.append(row)

for i in range(rows):
    row_sum = 0
    for j in range(columns):
        row_sum +=matrix[i][j]
    print(f"Sum of row {i+1} = {row_sum}")

# Enter the number of rows: 3
# Enter the number of columns:3
# Enter the elements of row 1: 4 9 5
# Enter the elements of row 2: 12 5 9
# Enter the elements of row 3: 6 7 4
# Sum of row 1 = 18
# Sum of row 2 = 26
# Sum of row 3 = 17