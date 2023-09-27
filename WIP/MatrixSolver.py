given_matrix = []


# Prints the given matrix
def show_matrix():
    for x in given_matrix:
        print(x)


# gives a row that is multiplied by a given number
def multiply_row(row, constant):
    temp_row = []
    for x in row:
        temp_row.append(x * constant)
    return temp_row


# Making the properly sized matrices with default values
num_rows = int(input("How many Rows ?\n"))
num_cols = int(input("How many Columns ?\n"))
i = num_rows
while i > 0:
    current_row_given = []
    j = num_cols
    while j > 0:
        current_row_given.append("_")
        j -= 1
    given_matrix.append(current_row_given)
    i -= 1


# Assigning values
i = 0
j = 0
while i < num_rows:
    while j < num_cols:
        given_matrix[i][j] = '*'
        show_matrix()
        given_matrix[i][j] = float(input("Highlighted cell value: "))
        j += 1
    j = 0
    i += 1


# Solving
# since dividing introduces a lot of error and it's difficult to store 2 numbers per cell
# only multiply rows in the matrix, divide at the end

# Getting to EF

# current_col is the column that has a variable being eliminated
current_col = 0
while current_col < num_cols:
    operating_row = current_col + 1
    coefficient_product = 1
    for x in given_matrix:
        coefficient_product *= x[current_col]
    multiplied_subtract = multiply_row(given_matrix[current_col], (coefficient_product / current_col[current_col]))
    while operating_row < len(given_matrix):
        # multiplied_row: variable going to 0
        multiplied_row = multiply_row(given_matrix[operating_row], (coefficient_product / current_col[operating_row]))
        given_matrix[operating_row] = multiplied_row - multiplied_subtract
        # ^ check this logic, syntax error ^
        operating_row += 1

    current_col += 1
# need to use that to eliminate that col in all other rows


# Tests
print("Matrix:")
show_matrix()
test_row = [1.0, 2.0, 3.0]
print("Test row: ", test_row)
test_row = multiply_row(test_row, 3)
print("Modified row: ", test_row)
