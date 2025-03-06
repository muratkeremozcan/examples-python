# Import pandas
import pandas as pd

# Load the CSV file
df = pd.read_csv('world_indicators_simple.csv')
print(df)

# Get the column names (row -1)
feature_names = df.columns.tolist()
# print(feature_names)

# Get the first row values
row_vals = df.iloc[0].tolist()
# print(row_vals)

#  Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)


###########
# function version

def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict


print(lists2dict(feature_names, row_vals))

# #######

# Get multiple rows from the DataFrame (not just the first row)
row_lists = [df.iloc[i].tolist() for i in range(len(df))]

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Create a list of dictionaries - one for each row
# [output_if_true | for variable in iterable | if condition]
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])

# Turn list of dicts back into a DataFrame: df
df_from_dicts = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df_from_dicts.head())