import pandas as pd

# Initialize an empty dictionary: counts_dict
from typing import Dict, Union, Optional

# In this context, counts_dict is a counter of occurrences
# Keys are likely strings from CSV columns, values are counts
# For CSV data, keys could be strings, ints, floats, etc. depending on column type
counts_dict: Dict[Union[str, int, float], int] = {}

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

def count_entries(csv_file: str, c_size: int, col_name: str) -> Dict[Union[str, int, float], int]:
	"""Return a dictionary with counts of occurrences as value for each key.
	
	Parameters:
	-----------
	csv_file : str
		Path to the CSV file
	c_size : int
		Chunk size for reading the CSV
	col_name : str
		Name of the column to count
	
	Returns:
	--------
	Dict[Union[str, int, float], int]
		Dictionary with column values as keys and counts as values
	"""

	counts_dict: Dict[Union[str, int, float], int] = {}

	for chunk in pd.read_csv(csv_file, chunksize=c_size):
		for entry in chunk[col_name]:
			if entry in counts_dict.keys():
				counts_dict[entry] += 1
			else:
				counts_dict[entry] = 1
	
	return counts_dict

result_counts = count_entries('tweets.csv', 10, 'lang')

print(result_counts)
