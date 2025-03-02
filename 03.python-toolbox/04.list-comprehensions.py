# list comprehensions collapse for loops for building lists into a single line

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

for doc in doctor:
	print(doc)

# list comprehension version
[print(doc) for doc in doctor]

# print first char of each string
for doc in doctor:
	print(doc[0])

[print(doc[0]) for doc in doctor]

##############

# Using the range of numbers from 0 to 9 as your iterable  and i as your iterator variable, 
# write a list comprehension that produces a list of numbers consisting of the squared values of i.

[i**2 for i in range(0, 10)]

##############

# recreate this with list comprehension
# matrix = [[0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4]]

# 1 row
print([col for col in range(5)])

# matrix
print([[col for col in range(5)] for row in range(5)])
[[col for col in range(5)] for row in range(5)]

# for loop version

matrix = []
for col in range(5): # rows
	row_list = [] # empty list for each row
	for row in range(5): # columns
		row_list.append(col) # # append col value to row
	matrix.append(row_list) # append the row to the matrix

# function versions
matrix_lambda = lambda rows, cols: [[col for col in range(cols)] for row in range(rows)]
print(matrix_lambda(5, 5))

def create_matrix(rows, cols):
	matrix = []
	for col in range(rows): #rows
		row_list = [] # empty list for each row
		for row in range(cols): # columns
			row_list.append(col) # append col value to row
		matrix.append(row_list)
	return matrix

print(create_matrix(5,5))