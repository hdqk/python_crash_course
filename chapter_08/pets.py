def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# This is an example of positional arguments
describe_pet('harry', 'hamster')

# This is an example of keyword arguments
describe_pet(animal_type='dog', pet_name='willie')

# This is an example of passing one argument and using the default
describe_pet('chief')
