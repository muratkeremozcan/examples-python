import numpy as np

# using %timeit in multi-line code is inefficient
# so we use code-profiling

# %load_ext line_profiler
# command for line-by-line 
# %lprun -f fn-name fn-name(args)

def convert_units(heroes, heights, weights):

	new_hts = [ht * 0.39370  for ht in heights]
	new_wts = [wt * 2.20462  for wt in weights]

	hero_data = {}

	for i,hero in enumerate(heroes):
			hero_data[hero] = (new_hts[i], new_wts[i])

	return hero_data


heroes = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman"]
hts = np.array([191, 183, 182, 175, 188])
wts = np.array([107, 95, 75, 70, 90])

# to profile this code, you would:

# Run the code in an IPython environment (like Jupyter Notebook)
# to load the extension: %load_ext line_profiler 
#  to see the detailed line-by-line profiling results:  %lprun -f convert_units convert_units(heroes, hts, wts)