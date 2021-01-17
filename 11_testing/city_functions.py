def get_formatted_city_name(city_name, country_name, population=''):
    """Generate a neatly formatted city - country name."""
    if population:
        formatted_name = f"{city_name.title()}, {country_name.title()} - population {population}"
    else:
        formatted_name = f"{city_name.title()}, {country_name.title()}"
    return formatted_name

print(get_formatted_city_name('santiago', 'chile', '5000000'))
print(get_formatted_city_name('athens', 'greece'))
