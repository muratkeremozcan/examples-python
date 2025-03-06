# Open a connection to the file
with open('world_indicators_simple.csv', 'r') as file:

    # Skip the column names
		file.readline()

    # Initialize an empty dictionary: counts_dict
		counts_dict: dict[str, int] = {}

    # Process only the first 10 rows
		for j in range(10):

        # Split the current line into a list: line
				line = file.readline().strip().split(',')

        # Get the value for the first column: first_col
				first_col = line[0]

        # If the column value is in the dict, increment its value
				if first_col in counts_dict.keys():
					counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
				else:
					counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)


############
# What if you want to do this for the entire file?
# In this case, it would be useful to use generators. Generators allow users to lazily evaluate data.

def read_large_file(file_object):
		"""A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
		while True:
			# Read a line from the file: data
			data = file_object.readline()
			
			# Break if this is the end of the file
			if not data:
				break

			# Yield the line of data
			yield data


# open a connection to the file
with open('world_indicators_simple.csv') as file:
	# Create a generator object for the file: gen_file
	gen_file = read_large_file(file)

	# Print the first three lines of the file
	print(next(gen_file))
	print(next(gen_file))
	print(next(gen_file))


####

counts_dict2: dict[str, int] = {}

with open('world_indicators_simple.csv') as file:
	# Iterate over the generator from read_large_file()
	# use the generator function
	for line in read_large_file(file):

		# Remove any leading/trailing spaces and split
		row = line.strip().split(',')

		# extract first column value
		first_col = row[0]

		# If the column value is in the dict, increment its value
		if first_col in counts_dict2.keys():
			counts_dict2[first_col] += 1

		# Else, add to the dict and set value to 1
		else:
			counts_dict2[first_col] = 1


print(counts_dict2)
