# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Create a for loop to loop over flash and print the values in the list. Use person as the loop variable.
for f in flash:
	print(f)

# Create an iterator for the list flash and assign the result to superhero.
superhero = iter(flash)

# Print each of the items from superhero using next() 4 times.
print(next(superhero))
print(next(superhero))
# print(next(superhero))
# print(next(superhero))


#############

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
# print(next(small_value))
# print(next(small_value))

# Loop over range(3) and print the values

for v in range(3):
	print(v)

# # Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))


########

# Create a range object that would produce the values from 10 to 20 using range(). Assign the result to values.
values = range(10, 21)

# Print the range object
print(values)

# Use the list() function to create a list of values from the range object values. Assign the result to values_list.
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)