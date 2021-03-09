def chosing_car(manufacturer, model, **car_data):
    car_data['Manufacturer:'] = manufacturer
    car_data['Model'] = model
    return car_data

car_profile = chosing_car('Toyota',
                          'Camry',
                           Color= 'Blue',
                          Engine= 'Manual')
print(car_profile)
