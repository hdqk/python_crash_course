def make_album(artist, title):
    """return dictionary containing artist and album"""
    album = {'artist': artist, 'title': title}
    return album


while True:
    print("Please enter the artist's info: ")
    print("(enter 'q' at any time to quit)")
    a_name = input("Artist's name: ")
    if a_name == 'q' or a_name == 'quit':
        break
    a_title = input("Album title: ")
    if a_title == 'q' or a_title == 'quit':
        break
    print(make_album(a_name.lower(), a_title.lower()))
