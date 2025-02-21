inflation_september = 3.2
inflation_august = 3.5

# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
	print('Inflation decreased')
else:
	print('Inflation increased')

#########



# Define your requirements
min_num_beds = 2
min_sq_foot = 750
max_rent = 1900

# Property details (example values)
num_beds = 3
sq_foot = 800
rent = 1800


if num_beds < min_num_beds:
	print('Too few beds')
elif sq_foot < min_sq_foot:
	print('Too small square foot')
elif rent > max_rent:
	print('Rent is too high')
else:
	print('Property meets requirements')