# namedtuple creates an immutable object with named fields (prop access)
# Provides cleaner attribute-style access (entry.species) instead of dict key lookup.

from collections import namedtuple

weight_log = [
	('Gentoo', 'MALE', 5500.0),
	('Chinstrap', 'MALE', 4300.0),
	('Adlie', 'MALE', 3800.0),
	('Gentoo', 'MALE', 5800.0),
	('Chinstrap', 'MALE', 4100.0),
	('Adlie', 'MALE', 3975.0),
	('Gentoo', 'MALE', 5400.0),
	('Chinstrap', 'MALE', 4800.0),
	('Chinstrap', 'FEMALE', 3800.0),
	('Adlie', 'FEMALE', 3450.0),
	('Chinstrap', 'MALE', 3950.0),
	('Gentoo', 'MALE', 5250.0),
	('Gentoo', 'FEMALE', 4300.0),
	('Gentoo', 'MALE', 4925.0),
	('Adlie', 'FEMALE', 3550.0),
	('Adlie', 'MALE', 3950.0),
	('Chinstrap', 'MALE', 3800.0),
	('Chinstrap', 'MALE', 4050.0),
	('Adlie', 'MALE', 3650.0),
	('Adlie', 'FEMALE', 3175.0),
]

SpeciesDetails = namedtuple('SpeciesDetails', ['species', 'sex', 'body_mass'])
print(SpeciesDetails('a', 'b', 'c'))

labeled_entries = []

for species, sex, body_mass in weight_log:
	labeled_entries.append(SpeciesDetails(species, sex, body_mass))

print(labeled_entries)
print(labeled_entries[:5])
print(labeled_entries[1].species)
# [
# 	SpeciesDetails(species='Gentoo', sex='MALE', body_mass=5500.0),
# 	SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=4300.0),
# 	SpeciesDetails(species='Adlie', sex='MALE', body_mass=3800.0),
# 	SpeciesDetails(species='Gentoo', sex='MALE', body_mass=5800.0),
# 	SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=4100.0),
# 	SpeciesDetails(species='Adlie', sex='MALE', body_mass=3975.0),
# 	SpeciesDetails(species='Gentoo', sex='MALE', body_mass=5400.0),
# 	SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=4800.0),
# 	SpeciesDetails(species='Chinstrap', sex='FEMALE', body_mass=3800.0),
# 	SpeciesDetails(species='Adlie', sex='FEMALE', body_mass=3450.0),
# 	SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=3950.0),
# 	SpeciesDetails(species='Gentoo', sex='MALE', body_mass=5250.0),
# 	SpeciesDetails(species='Gentoo', sex='FEMALE', body_mass=4300.0),
# 	SpeciesDetails(species='Gentoo', sex='MALE', body_mass=4925.0),
# 	SpeciesDetails(species='Adlie', sex='FEMALE', body_mass=3550.0),
# 	SpeciesDetails(species='Adlie', sex='MALE', body_mass=3950.0),
# 	SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=3800.0),
# 	SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=4050.0),
# 	SpeciesDetails(species='Adlie', sex='MALE', body_mass=3650.0),
# 	SpeciesDetails(species='Adlie', sex='FEMALE', body_mass=3175.0),
# ]

for entry in labeled_entries[:20]:
	if(entry.species == 'Chinstrap'):
		print(f'{entry.sex}:{entry.body_mass}')