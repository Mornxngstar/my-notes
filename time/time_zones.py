from datetime import datetime
import pytz

def run():
    def get_time_zone(city:str,continent:str) -> str:
        city_tz = pytz.timezone(f'{continent}/{city}')
        city_date = datetime.now(city_tz)
        return city_date.strftime('%d/%m/%Y  -  %H:%M:%S')
    
    data = input("Enter the city and its continent followed by a '-'\n\n")
    index = data.find('-')
    city = data[:index].capitalize()
    continent = data[index+1:].capitalize()

    date_time = get_time_zone(city, continent)
    print(f"Your city's date time is: {date_time}")

if __name__ == '__main__':
    run()
