class Song:
    count = 0  # Class attribute to keep track of the number of songs
    genres = []  # Class attribute to store unique genres
    artists=[]
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()  # Call the class method to increment count
        Song.add_to_genres(genre)  # Call the instance method to add genre to genres list
        Song.add_to_artist(artist)
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1  # Increment the count using the class method
    @classmethod
    def add_to_genres(cls,genre):
        if genre not in Song.genres:
            Song.genres.append(genre)  # Add unique genres to the class attribute
    @classmethod
    def add_to_artist(cls,artist):
        if artist not in Song.artists:
            Song.artists.append(artist)
# Example usage:
song1 = Song("Title 1", "Artist 1", "Genre 1")
print(Song.genres)  # Output: ['Genre 1']

song2 = Song("Title 2", "Artist 2", "Genre 2")
print(Song.genres)  # Output: ['Genre 1', 'Genre 2']

song3 = Song("Title 3", "Artist 3", "Genre 1")  # Adding a song with a genre that already exists
print(Song.genres)  # Output: ['Genre 1', 'Genre 2']
song4 = Song("title4","Article 3","gg")
print(Song.genres)
print(Song.count)
print(Song.artists)