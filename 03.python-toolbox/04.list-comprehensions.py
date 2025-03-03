# list comprehensions collapse for loops for building lists into a single line

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

for doc in doctor:
	print(doc)

# list comprehension version
[print(doc) for doc in doctor]

# map version
(list(map(print, doctor)))

# print first char of each string
for doc in doctor:
	print(doc[0])

[print(doc[0]) for doc in doctor]

# map version
list(map(lambda doc: print(doc[0]), doctor))

##############

# Using the range of numbers from 0 to 9 as your iterable  and i as your iterator variable, 
# write a list comprehension that produces a list of numbers consisting of the squared values of i.

[i**2 for i in range(0, 10)]

# for loop version
squared_numbers = []
for i in range(10):
	squared_numbers.append(i**2)
print(squared_numbers)

# map version
list(map(lambda i: i**2, range(0, 10)))


##############

# recreate this with list comprehension
# matrix = [[0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4]]

# 1 row
print([col for col in range(5)])

# for loop version
row_list = []
for col in range(5):
	row_list.append(col)
print(row_list)

# map version
row_list_map = list(map(lambda col: col, range(5)))
print(row_list_map)

## matrix

# list comprehension version
matrix_comp = [[col for col in range(5)] for row in range(5)]
print(matrix_comp)

# map version
matrix_map = list(map(lambda _: list(map(lambda col: col, range(5))), range(5)))

# for loop version

matrix = []
for col in range(5): # rows
	row_list = [] # empty list for each row
	for row in range(5): # columns
		row_list.append(col) # # append col value to row
	matrix.append(row_list) # append the row to the matrix

# function versions
matrix_lambda_comp = lambda rows, cols: [[col for col in range(cols)] for row in range(rows)]
print(matrix_lambda_comp(5, 5))

# Lambda function for matrix creation
matrix_lambda_map = lambda rows, cols: list(map(lambda _: list(map(lambda col: col, range(cols))), range(rows)))

print(matrix_lambda_map(5, 5))


def create_matrix(rows, cols):
	matrix = []
	for col in range(rows): #rows
		row_list = [] # empty list for each row
		for row in range(cols): # columns
			row_list.append(col) # append col value to row
		matrix.append(row_list)
	return matrix

print(create_matrix(5,5))