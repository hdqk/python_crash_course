def make_shirt(size='large', message='I love Python'):
    """print sentence with size and message"""
    print(f"This t-shirt is a {size.title()}, and reads: {message}.")


make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='Happy wife, happy life')
