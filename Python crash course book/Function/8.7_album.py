def make_album(artist_name, album_title, no_of_songs = None):
    
    album = {
        "Artist": artist_name,
        "Title" : album_title
    }
    
    if no_of_songs:
        album["Total songs"] = no_of_songs
        
    return album

active_polling = True
albums = {}
while active_polling:
    
    artist_name = input("Enter the artist name: ")
    if artist_name == "quit":
        break
    
    album_title = input("Enter the album name: ")   
    if album_title == "quit":
        break
     
    total_songs = input("Enter the total songs: ")
    if total_songs == "quit":
        break
        

    album = make_album(artist_name, album_title, total_songs)
    print(album)

    albums[album_title] = album

print(albums)