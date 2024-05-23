# Hector Delgado 5/15/2024

def city_country(city, country, population=''):
    """Returns a neatly formatted 'City, Country'"""
    if population:
        formatted_name = f"{city.title()}, {country.title()
                                            } - population {population}"
    else:
        formatted_name = f"{city.title()}, {country.title()}"
    return formatted_name
