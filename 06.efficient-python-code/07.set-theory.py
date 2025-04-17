# set's difference with list/array: unique elements, no index access
# Use set() to convert lists into sets for uniqueness.
# difference() finds elements in one set but not in another.
# union() merges sets, keeping unique values.
# intersection() finds common elements between sets.
# len(set) returns the number of unique elements.

ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']
misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']

# set(..) converts an array to a set
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# set1.intersection(set2) wills show the intersection
both = ash_set.intersection(misty_set)
print(both)