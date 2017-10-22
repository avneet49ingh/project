import amadeus
#from amadeus import RailStations
#rails = RailStations('jJo9Nv9JifWAIXFanTiV2tSAXRHFHEWc')
from amadeus import Cars

cars = Cars('jJo9Nv9JifWAIXFanTiV2tSAXRHFHEWc')
resp = cars.search_airport(
    pick_up='2017-12-18',
    drop_off='2017-12-23',
    location='BLR',
    currency='USD',
    lang='EN')
print("testing")
print(resp)
