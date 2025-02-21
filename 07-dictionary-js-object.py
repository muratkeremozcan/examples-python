playlist_list = [1, "Blinding Lights", "The Weeknd", 
                 2, "One Dance", "Drake", 
                 3, "Uptown Funk", "Mark Ronson", 
                 4, "Closer", "The Chainsmokers",
                 5, "One Kiss", "Calvin Harris", 
                 6, "Mr. Brightside", "The Killers"]


# Extract the first two songs
playlist_dict = {
  playlist_list[2]: playlist_list[1],
  playlist_list[5]: playlist_list[4]
}

print(playlist_dict)

# full playlist
playlist = {playlist_list[i + 2]: playlist_list[i + 1] for i in range(0, len(playlist_list), 3)}
print(playlist)