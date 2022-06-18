
cities_in_F = {"New York" : 32, "Boston" : 75, "Los Angeles" : 100, "Chicago" : 50}
cites_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}


wather = {"New York" : "cold", "Boston" : "sunny", "Los Angeles" : "sunny", "Chicago" : "cloudy"}
sunny_wheater = {key:value for (key,value) in wather.items() if value == "sunny" }

cities = {"New York" : 32, "Boston" : 75, "Los Angeles" : 100, "Chicago" : 50}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}



def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {"New York" : 32, "Boston" : 75, "Los Angeles" : 100, "Chicago" : 50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}

print(desc_cities)