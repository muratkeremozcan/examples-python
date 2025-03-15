#	Tuple unpacking and dictionary creation are powerful techniques in Python for organizing data.
#	Converting structured data into a dictionary makes it more accessible.
#	Sorting dictionaries by key allows structured outputs.
# Safe-access dictionaries with get() 

squirrels = [
	('Marcus Garvey Park', ('Black', 'Cinnamon', 'Cleaning', None)),
	('Highbridge Park', ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree')),
	('Madison Square Park', ('Gray', None, 'Foraging', 'Indifferent')),
	('City Hall Park', ('Gray', 'Cinnamon', 'Eating', 'Approaches')),
	('J. Hood Wright Park', ('Gray', 'White', 'Running', 'Indifferent')),
	('Seward Park', ('Gray', 'Cinnamon', 'Eating', 'Indifferent')),
	('Union Square Park', ('Gray', 'Black', 'Climbing', None)),
	('Tompkins Square Park', ('Gray', 'Gray', 'Lounging', 'Approaches'))
]

squirrels_by_park = {}

for park, squirrel_details in squirrels:
	squirrels_by_park[park] = squirrel_details

print(squirrels_by_park)
# {
#     'Marcus Garvey Park': ('Black', 'Cinnamon', 'Cleaning', None),
#     'Highbridge Park': ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree'),
#     'Madison Square Park': ('Gray', None, 'Foraging', 'Indifferent'),
#     'City Hall Park': ('Gray', 'Cinnamon', 'Eating', 'Approaches'),
#     'J. Hood Wright Park': ('Gray', 'White', 'Running', 'Indifferent'),
#     'Seward Park': ('Gray', 'Cinnamon', 'Eating', 'Indifferent'),
#     'Union Square Park': ('Gray', 'Black', 'Climbing', None),
#     'Tompkins Square Park': ('Gray', 'Gray', 'Lounging', 'Approaches')
# }


for park in sorted(squirrels_by_park):
	print(f'{park}: {squirrels_by_park[park]}')
# City Hall Park: ('Gray', 'Cinnamon', 'Eating', 'Approaches')
# Highbridge Park: ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree')
# J.Hood Wright Park: ('Gray', 'White', 'Running', 'Indifferent')
# Madison Square Park: ('Gray', None, 'Foraging', 'Indifferent')
# Marcus Garvey Park: ('Black', 'Cinnamon', 'Cleaning', None)
# Seward Park: ('Gray', 'Cinnamon', 'Eating', 'Indifferent')
# Tompkins Square Park: ('Gray', 'Gray', 'Lounging', 'Approaches')
# Union Square Park: ('Gray', 'Black', 'Climbing', None)


#############
# safe-access with get(), the 2nd arg is the default return if nothing is found (otherwise things error)
print(squirrels_by_park.get('Union Square Park'))
print(type(squirrels_by_park.get('Fort Tryon Park')))
print(squirrels_by_park.get('Central Park', 'Not Found'))
