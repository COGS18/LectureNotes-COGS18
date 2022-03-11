class Playlist:
    
    def __init__(self, title):
        self.title = title
        self.song_list = []
        self.length = 0
        
    def add_song(self, song_title):
        if song_title not in self.song_list:
            self.song_list.append(song_title)
            self.length += 1
            
    def remove_song(self, song_title):
        self.song_list.remove(song_title)
        self.length -= 1
        
    def find_artist(self, song_title):
        for i in self.song_list:
            if song_title in i.keys():
                return i[song_title]
            
# finds the number of unique artists in a single playlist and returns the number
def artist_count(playlist):
    artist_list = []
    for i in playlist.song_list:
        song_title = list(i.keys())[0]
        artist = playlist.find_artist(song_title)
        if artist not in artist_list:
            artist_list.append(artist)
    num_artists = len(artist_list)
    if num_artists == 1:
        return 'There is 1 artist in {}'.format(playlist.title)
    else:
        return 'There are {} artists in {}'.format(num_artists, playlist.title)
    
# finds the playlist in a list of playlists which has the most unique artists
def most_unique(playlist_list):
    max_artists = 0
    playlist = ''
    for i in playlist_list:
        artist_list = []
        for j in i.song_list:
            song_title = list(j.keys())[0]
            artist = i.find_artist(song_title)
            if artist not in artist_list:
                artist_list.append(artist)
        num_artists = len(artist_list)
        if num_artists >= max_artists:
            max_artists = num_artists
            playlist = i
    
    return '{} has the most unique artists, with {} artists'.format(playlist.title, max_artists)
