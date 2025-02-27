# try except (like try catch)
# keeps executing even if try block fails

def snake_case(text):
  # Use a keyword allowing you to attempt to run code that cleans text
  try:
    # swap a space for a single underscore in the text argument.
    return text.replace(' ', '_').lower()
  # Run this code if an error occurs
  except:
    print('The snake_case() function expects a string as an argument, please check the data type provided.')
    return None


# raise  (isn't like anything in JS)
# halts execution on error
    
print(snake_case('User Name 187'))
# print(snake_case2(123))

def snake_case2(text):
  # Check the data type
  if isinstance(text, str):
    return text.replace(' ', '_').lower()     

  else: 
    raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")
  
print(snake_case2('User Name 187'))
# print(snake_case2(123))