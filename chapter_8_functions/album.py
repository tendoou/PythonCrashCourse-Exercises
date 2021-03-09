def artist_game(artist, album, year=None, song=None):
    album = {
        'artist': artist.title(),
        'album': album.title()
    }

    if song:
        album['song'] = song
    if year:
        album['year'] = year
    return album


while True:
    print("Please chose an album of your favorite artist")
    print("Press 'q' anytime to exit")
    r_artist = input("Artist:")
    if r_artist == 'q':
        break
    while r_artist == '':
        print("It's necessary to chose an artist")
        r_artist = input("Artist:")

    r_album = input("Chose an album:")
    if r_album == 'q':
        break

    while r_album == '':
        print("You have to chose an album")
        r_album = input("Album:")

    r_year = input('Year (optional):')
    if r_year == 'q':
        break

    r_song = input("Favorite song (optional):")
    if r_song == 'q':
        break

    favorite_artist = artist_game(r_artist, r_album, r_year, r_song)
    print(favorite_artist)