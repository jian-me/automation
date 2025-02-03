#
# Python script generated via AI in Tines to calculate the distance between two points using the Haversine method
# 

from math import radians, cos, sin, asin, sqrt

def main(input):
    p1_lat = float(input.get('point_1', {}).get('latitude'))
    p1_lon = float(input.get('point_1', {}).get('longitude'))
    p2_lat = float(input.get('point_2', {}).get('latitude'))
    p2_lon = float(input.get('point_2', {}).get('longitude'))

    def haversine(lat1, lon1, lat2, lon2):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers
        return c * r

    distance_km = haversine(p1_lat, p1_lon, p2_lat, p2_lon)
    distance_miles = distance_km * 0.621371
    distance_nautical = distance_km * 0.539957

    return {
        'distance_km': distance_km,
        'distance_miles': distance_miles,
        'distance_nautical': distance_nautical
    }