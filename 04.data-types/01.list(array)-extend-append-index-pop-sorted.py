baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Use .extend() to add multiple elements at once
# This prevents nesting issues that would occur with .append()
baby_names.extend(['Rowen', 'Sandeep'])

# Find the position (index) of 'Rowen' in the list
position = baby_names.index('Rowen')

# Remove 'Rowen' using its position
# .pop() deletes and returns the value at the given index
baby_names.pop(position)

# Print the final list after modifications
print(baby_names)

# with append, nesting can occur if we are passing an array
baby_names.append('Murat')
print(baby_names)

baby_names.append(['Kerem', 'Ozcan'])
print(baby_names)


#########
# List comprehensions provide a concise way to transform lists.
# Use sorted() to return a new sorted list without modifying the original.

# List of lists (each entry contains: Year, Gender, Count, Name)
records = [
    ['2014', 'F', '20799', 'Emma'],
    ['2014', 'M', '18656', 'Noah'],
    ['2014', 'F', '19674', 'Olivia'],
    ['2014', 'M', '18399', 'Liam'],
]

# [output_if_true | for variable in iterable]
baby_names = [row[3] for row in records]
    
# sorted(..) sorts in alphabetical order
print(sorted(baby_names))