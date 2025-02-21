# sets
# mutable collection that only stores unique elements.

my_set = {1, 2, 3, 4, 4, 5}  # Duplicate "4" is removed
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Add an element
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Check if an element exists
print(3 in my_set)  # Output: True

# Remove an element
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5, 6}


#####
# tuples
# immutable collection that can store duplicate values

q3_financials = (325780, 1041, 4271599)


#### 

# Create a set for indie artists
indie_set = {"Kings of Leon", "Arctic Monkeys", "Stereophonics"}
print(indie_set)

# array to set
hip_hop = ["Drake", "JAY-Z", "50 Cent", "Drake"]
hip_hop_set = set(hip_hop)
print(hip_hop_set)