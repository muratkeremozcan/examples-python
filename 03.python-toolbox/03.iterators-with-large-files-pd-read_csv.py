import pandas as pd

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# define the chunk size
chunk_size = 10

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv', chunksize=chunk_size):

    # Iterate over the 'lang' column in the current chunk
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)

def count_entries(csv_file, c_size, col_name):
	"""Return a dictionary with counts of
  occurrences as value for each key."""

	counts_dict = {}

	for chunk in pd.read_csv(csv_file, chunksize=c_size):
		for entry in chunk[col_name]:
			if entry in counts_dict.keys():
				counts_dict[entry] += 1
			else:
				counts_dict[entry] = 1
		
		return counts_dict

result_counts = count_entries('tweets.csv', 10, 'lang')

print(result_counts)
