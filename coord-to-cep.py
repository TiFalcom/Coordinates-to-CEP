import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

def get_cep(address):
    location = address.split(",")
    return location[len(location)-2]

def get_address(location):
    return location.address

path = input("Insert the file path, without file name: ")
filename = input("Insert the file full name: ")

df = pd.read_csv(path + '\\' + filename, sep='\t')
#df = pd.DataFrame({'COORDS': ['-23.538918, -46.793696', '-23.478389, -46.864268', '-23.514244, -46.445519']})

geolocator = Nominatim(user_agent="coord-to-cep")
location = RateLimiter(geolocator.reverse, min_delay_seconds=1)

df['LOCATION'] = df['COORDS'].apply(location)
df['ADDRESS'] = df['LOCATION'].apply(get_address)
df['CEP'] = df['ADDRESS'].apply(get_cep)
df.pop('LOCATION')

df.to_csv(path + '\EXPORT_CEPS.CSV', index = False)