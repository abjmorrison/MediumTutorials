from geopy.geocoders import Nominatim
from ratelimiter import RateLimiter

@RateLimiter(max_calls=10, period=1)
def geocode(df, column):

    df_dict = dict(zip(df.index, df.location))
    valid_types = ['city','village']
    valid_countries = ['Democratic Republic of the Congo','République démocratique du Congo']
    matches = []

    for k, v in df_dict.items():
        locs = geolocator.geocode(v, exactly_one=False)
        if locs != None:
            for l in locs:
                if l.raw['type'] in valid_types:
                    lat = l.raw['lat']
                    long = l.raw['lon']
                    name = l.raw['display_name']
                    if 'Congo' in name:
                        matches.append({k : [name, lat, long]})
                    else: continue
                else: continue

    return matches
