import pandas as pd
import matplotlib.pyplot as plt
#  initialize reader object: df_reader
import os

# Get path to current directory
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'ind_pop_data.csv')


                         


# iterate over each DataFrame chunk
def plot_pop(filename, country_code):
	# Initialize empty DataFrame: data
	data = pd.DataFrame()

	# Initialize reader object: urb_pop_reader with proper CSV handling
	# Use quoting and escaping to handle country names with commas
	urb_pop_reader = pd.read_csv(filename, chunksize=10, quotechar='"', escapechar='\\', on_bad_lines='warn')
		
	for df_urb_pop in urb_pop_reader:

		# check out specific country
		df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

		# zip DataFrame columns of interest: pops
		pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Value'])

		# Turn zip object into list: pops_list
		pops_list = list(pops)

		# Use list comprehension to create new DataFrame column 'Total Urban Population'
		df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

		# Concatenate DataFrame chunk to the end of data: data
		data = pd.concat([data, df_pop_ceb]) # merge chunks progressively

	# plot urban population data
	data.plot(kind='scatter', x='Year', y='Total Urban Population')
	plt.show()

plot_pop(csv_path, 'CEB')