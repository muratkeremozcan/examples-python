# A numpy array contains homogeneous data types (which reduces memory consumption) 
# and provides the ability to apply operations on all elements


import numpy as np

nums = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Print second row of nums
print(nums[1, :])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:, 2] = nums[:, 2] + 1
print(nums)

####################
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

arrival_times = [*range(10, 60, 10)]
print(arrival_times)

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3
print(new_times)
print(*enumerate(new_times))

# Use list comprehension and enumerate to pair guests to new times
# [output_if_true | for variable in iterable | if condition]
guest_arrivals = [(names[i], time) for i, time in enumerate(new_times)]
print(guest_arrivals)

def welcome_guest(guest):
	name, time = guest
	return f"Welcome {name}! You arrived {time} minutes late."

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(guest_welcomes)

print(*guest_welcomes, sep='n')