import pandas as pd

# Load the csv file
df = pd.read_csv('tweets.csv')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
# Use list comprehension to extract characters 11:19 (0-based indexing) from each timestamp
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)

tweet_clock_time2 = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']
print(tweet_clock_time2)
