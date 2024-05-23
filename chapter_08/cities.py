def describe_city(city, country='the united states'):
    """prints the city and it's country"""
    print(f"{city.title()} is in {country.title()}.")


describe_city('Boston')
describe_city('New Delhi', country='India')
describe_city(city='London', country='England')
