import pandas as pd
import numpy as np

baseball_df = pd.DataFrame({
	'Team': ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'PHI', 'PIT', 'SFG', 'STL', 'WSA'],
	'League': ['NL', 'NL', 'AL', 'AL', 'NL', 'NL', 'NL', 'NL', 'NL', 'AL'],
	'Year': [2012, 2012, 2012, 2012, 2012, 1962, 1962, 1962, 1962, 1962],
	'RS': [734, 700, 712, 734, 613, 705, 706, 878, 774, 599],  # Runs Scored
	'RA': [688, 600, 705, 806, 759, 759, 626, 690, 664, 716],  # Runs Allowed
	'W': [81, 94, 93, 69, 61, 81, 93, 103, 84, 60],            # Wins
	'G': [162, 162, 162, 162, 162, 161, 161, 165, 163, 162],   # Games
	'Playoffs': [0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
})

def calc_win_perc(wins, games_played):
	win_perc = wins / games_played
	return np.round(win_perc,2)

win_percs_list = []

for i in range(len(baseball_df)):
	row = baseball_df.iloc[i]

	wins = row['W']
	games_played = row['G']

	win_perc = calc_win_perc(wins, games_played)

	win_percs_list.append(win_perc)

baseball_df['WP'] = win_percs_list

print(baseball_df, '\n')