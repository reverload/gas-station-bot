from geopy.distance import geodesic

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on the Earth (specified in decimal degrees)
    using geopy's geodesic method.
    """
    return geodesic((lat1, lon1), (lat2, lon2)).kilometers

def find_nearest_stations(user_location, stations, number_of_stations=10):
    """
    Find the nearest gas stations to the user's location.

    Parameters:
    - user_location: A tuple containing the user's latitude and longitude.
    - stations: A list of dictionaries, where each dictionary contains information about a gas station,
                including its name, address, fuel prices, and geographical coordinates.
    - number_of_stations: The number of nearest stations to return.

    Returns:
    - A list of the nearest gas stations sorted by distance from the user's location.
    """
    user_lat, user_lon = user_location
    for station in stations:
        # Convert latitude and longitude from string to float, replacing commas with dots
        station_lat = float(station['Latitud'].replace(',', '.'))
        station_lon = float(station['Longitud (WGS84)'].replace(',', '.'))
        distance = calculate_distance(user_lat, user_lon, station_lat, station_lon)
        station['distance'] = distance

    # Sort stations by distance
    stations_sorted_by_distance = sorted(stations, key=lambda x: x['distance'])

    # Return the specified number of nearest stations
    return stations_sorted_by_distance[:number_of_stations]
