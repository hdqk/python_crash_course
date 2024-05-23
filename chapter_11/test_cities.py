# Hector Delgado 5/15/2024

from city_functions import city_country


def test_city_country():
    """Do combinations like 'boston, usa' work?"""
    formatted_name = city_country('boston', 'united states')
    assert formatted_name == 'Boston, United States'


def test_city_country_population():
    """Do combinations like 'santiago, chile, 5000000' work?"""
    formatted_name = city_country('santiago', 'chile', '5000000')
    assert formatted_name == 'Santiago, Chile - population 5000000'
