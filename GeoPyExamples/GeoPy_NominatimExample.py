from geopy.geocoders import Nominatim
from ratelimiter import RateLimiter

@RateLimiter(max_calls=10, period=1)
def geocode(df, column, valid_types, valid_countries=None):
    '''
    This function uses the Nomintim service via GeoPy
    to geocode a list of place names
    This function accepts a data frame with a column of place names,
    a list of types that match the desired location type, and a list of country names that match the desired country
    '''

    df_dict = dict(zip(df.index, df['column']))
    matches = []

    for k, v in df_dict.items():
        locs = geolocator.geocode(v, exactly_one=False)
        if locs != None:
            for l in locs:
                if l.raw['type'] in valid_types:
                    lat = l.raw['lat']
                    long = l.raw['lon']
                    name = l.raw['display_name']
                    matches.append({k : [name, lat, long]})
                else: continue

    return matches
