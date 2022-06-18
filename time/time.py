from datetime import datetime

my_time = datetime.utcnow()
print(my_time)

latam_format = my_time.strftime('%d/%m/%Y')
print(f'Latam format: {latam_format}')

usa_format = my_time.strftime('%m/%d/%Y')
print(f'USA format: {usa_format}')

year = my_time.strftime("This is the year %Y")
print(year)
