def make_album(artist_name, title, no_of_songs = None):
    """function to store music details in a dictionary"""

    album = {}

    album["Artist Name"] = artist_name
    album["Album Title"] = title

    if no_of_songs:
        album["No of songs"] = no_of_songs
    

    return album

new_album = make_album("One direction", "What Makes you Beautiful", 10)

for k, v in new_album.items():
    print(k, v)