# Define clean_text, which has two arguments: text, and lower, 
# with the latter having a default value of True
raw_text = 'I LoVe dATaCamP'

def clean_text(text, lower = True):
	if lower == False:
		return text.replace(' ', '_')	
	else:
		return text.replace(' ', '_').lower()

print(clean_text(raw_text))

# Re-define clean_text with arguments of text followed by remove, 
# with the latter having a default value of None.

def clean_text_remove(text, remove = None):
	if remove != None:
		return text.replace(remove, '').lower()
	else:
		return text.lower()

print(clean_text_remove(raw_text, 'L'))

# named arguments option: different to JS, in Python we can specify the arg names if we want
# In JS we can only do this with objects
print(clean_text_remove(text = raw_text, remove = 'L'))


#####################
# Define convert_data_structure with two arguments: data and data_type,
# where the latter has a default value of "list".

def convert_data_structure(data, data_type = 'list'):
	# Add a condition to check if data_type is "tuple"
	if (data_type == 'tuple'):
		data = tuple(data)

	# Else if data_type is set, convert to a set
	elif (data_type == 'set'):
		data = set(data)	
	
	else:
		data = list(data)

	return data

some_data = {"a", 1, "b", 2, "c", 3}

# Call the function to convert to a set
print (convert_data_structure(some_data, data_type = 'set') )
