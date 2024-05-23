# Hector Delgado 5/8/2024

def car(manufacturer, model, **car_info):
    """prints the car's details in a dictionary"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car1 = car('toyota', 'camry', year=2017, color='silver')
print(car1)
