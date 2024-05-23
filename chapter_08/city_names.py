def city_country(city, country):
    """returns a city and country pair"""
    message = f"{city.title()}, {country.title()}"
    return message


print(city_country('santiago', 'chile'))
print(city_country(city='paris', country='france'))
print(city_country('moscow', 'russian'))
