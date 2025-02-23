# Types of Modules
# 	•	Built-in modules: These come with Python (e.g., math, random, datetime, string).
# 	•	User-defined modules: These are Python files you create yourself.
# 	•	Third-party modules: These are external libraries installed via pip (e.g., numpy, pandas).

# Import the string module
import string

# Print all ASCII lowercase characters
print(string.ascii_lowercase)

# Print all punctuation
print(string.punctuation)

##########

# Import date from the datetime module
from datetime import date 

# Create a variable called deadline
deadline = date(2024, 1, 19)

# Check the data type
print(type(deadline))

# Print the deadline
print(deadline)