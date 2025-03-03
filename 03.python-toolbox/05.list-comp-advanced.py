# using conditionals in comprehensions
# [ output expression for iterator variable in iterable if predicate expression ]

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
# Use member as the iterator variable in the list comprehension. 
# For the conditional, use len() to evaluate the iterator variable. 
# Note that you only want strings with 7 characters or more.

# [output_if_true | for variable in iterable | if condition]
new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)

# filter version
new_fellowship_filter = list(filter(lambda member: len(member) >= 7, fellowship))
print(new_fellowship_filter)

# In the output expression, keep the string as-is if the number of characters is >= 7, 
# else replace it with an empty string

# [output_if_true | if condition | else output_if_false | for variable in iterable]
new_fellowship2 = [member if len(member) >= 7 else '' for member in fellowship]
print(new_fellowship2)

new_fellowship2_map = list(map(lambda member: member if len(member) >= 7 else '', fellowship))
print(new_fellowship2_map)


######## Dict comprehension

# Create dict comprehension
new_fellowship_dict = {member: len(member) for member in fellowship if len(member) >= 7}
print(new_fellowship_dict)

# filter version
new_fellowship_filter_dict = dict(filter(lambda member: len(member[0]) >= 7, ((member, len(member)) for member in fellowship)))
print(new_fellowship_filter_dict)

###

new_fellowship2_map_dict = dict(map(lambda member: (member, member if len(member) >= 7 else ''), fellowship))
print(new_fellowship2_map_dict)