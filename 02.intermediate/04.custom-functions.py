# Define a function called clean_string, which takes an argument called text
def clean_string(text):
	# Replace spaces with underscores
	no_spaces = text.replace(' ', '_')
	# Convert to lowercase
	clean_text = no_spaces.lower()
	# Return the final text as an output	
	return clean_text

raw_text = 'I LoVe dATaCamP'
converted_text = clean_string('I LoVe dATaCamP')

print(converted_text)

####

def clean_string2(text):
	return text.replace(' ', '_').lower()

print(clean_string2(raw_text))

####

clean_string3 = lambda text: text.replace(' ', '_').lower()

print(clean_string3(raw_text))


##############
password = "not_very_secure_2023"

# Define the password_checker function
def password_checker(submission):
  
  # Check that the password variable and the submission match
  if submission == password:
    print("Successful login!")
  
  # Otherwise, print "Incorrect password"
  else:
    print("Incorrect password")

# Call the function    
password_checker(password)