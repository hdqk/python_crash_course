def make_album(artist, title, songs=None):
    """return dictionary containing artist and album"""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album


print(make_album('adele', '21'))
print(make_album('pink floyd', 'dark side of the moon'))
print(make_album('vanilla', 'origin', songs=17))
