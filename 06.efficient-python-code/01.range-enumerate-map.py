# - Use range(start, stop, step) to generate sequences; convert to lists with list(...) or [*...]
# - Use enumerate() to attach indices to list items, producing tuples (index, item)
# - [*enumerate(some_var, 1)] quickly converts an enumerate iterator (starting at 1) into a list of tuples

# Create a range object that goes from 0 to 5
nums = range(5)
print(type(nums))

# Convert nums to a list
nums_list = list(range(5))
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1, 12, 2)]
print(nums_list2)

# list(range(..)) same as [*range(..)]
num_list3 = list(range(1, 12, 2))
print(num_list3)

######### enumerate

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

indexed_names_0 = []
for i in range(len(names)):
    index_name = (i, names[i])
    indexed_names_0.append(index_name)
print(indexed_names_0)

# using enumerate
indexed_names = []
for i, name in enumerate(names):
	index_name = (i, name) # (0, 'Jerry')...
	indexed_names.append(index_name)
print(indexed_names)

# using list comprehension
# [output_if_true | for variable in iterable | if condition]
indexed_names_comp_0 = [(i, name) for i in enumerate(names)]
print(indexed_names_comp_0)

# in this version each tuple from enumerate(names) is automatically unpacked into the two variables i (the index) and name
indexed_names_comp = [(i,name) for i, name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack_0 = [*enumerate(names, 1)]
print(indexed_names_unpack_0)
indexed_names_unpack =  list(enumerate(names, 1))
print(indexed_names_unpack)


############ map
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]
print(names_uppercase)