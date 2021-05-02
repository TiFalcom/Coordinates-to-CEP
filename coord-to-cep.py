import pycep_correios
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="coord-to-cep")

location = geolocator.reverse("-23.677506, -46.540665")

address1 = location.address.split(",")
address2 = pycep_correios.get_address_from_cep(address1[8])

print(address2['logradouro'] + ", " + address2['cidade'] + " - " + address2['bairro'] + " - " + address1[8])