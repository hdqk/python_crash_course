# Hector Delgado 5/15/2024

from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'janis joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'


def test_first_last_middle_name():
    """Do names like 'wolfgang amadeus mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
