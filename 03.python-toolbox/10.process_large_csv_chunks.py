import pandas as pd
import matplotlib.pyplot as plt

#  initialize reader object: df_reader
import os

# Get path to current directory
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'ind_pop_data.csv')

df_reader = pd.read_csv(csv_path, chunksize=10)

print(next(df_reader))
print(next(df_reader))


#########
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv(csv_path, chunksize=10)

# get the first chunk
df_urb_pop = next(urb_pop_reader)

# check the head of the dataframe
print(df_urb_pop.head())

# check out specific country: df_pop_ceb

# access single column; the country code
print(df_urb_pop['CountryCode'])
# same column in boolean series
print(df_urb_pop['CountryCode'] == 'CEB')
# filter the DataFrame with Boolean Indexing
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
# JS: df_pop_ceb = df_urb_pop.filter(row => row.CountryCode === "CEB");
print(df_pop_ceb)

# Zip DataFrame columns of interest: pops
print(df_pop_ceb['Total Population'])
# The urban percentage is in the 'Value' column
print(df_pop_ceb['Value'])
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Value'])
print(pops)

# Turn zip object into list: pops_list
pops_list = list(pops)

print(pops_list)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
# Calculate Total Urban Population = Total Population × Urban percentage ÷ 100
df_pop_ceb['Total Urban Population'] = [int(pop[0] * pop[1] / 100) for pop in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()