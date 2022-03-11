import playlist as pl

my_playlist = pl.Playlist('Vibes')
my_playlist.add_song({'Comic Sans' : 'Audrey Nuna'})
my_playlist.add_song({'Why' : 'Dominic Fike'})
my_playlist.add_song({'Yellow Cab' : 'DPR LIVE'})
my_playlist.add_song({'zombie pop' : 'DPR IAN'})
my_playlist.add_song({'Blossom' : 'Audrey Nuna'})
my_playlist.add_song({'Dive with you (feat. eaJ)' : 'Seori, eaJ'})
print(my_playlist.song_list)
print(pl.artist_count(my_playlist))