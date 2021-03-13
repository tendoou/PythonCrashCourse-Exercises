def get_full_city_name(city, country, population=""):
    if not population:
        full_city_name = f"{city.title()}, {country.title()}"
    else:
        full_city_name = f"{city.title()}, {country.title()} -" \
                         f" population {population}"
    return full_city_name
