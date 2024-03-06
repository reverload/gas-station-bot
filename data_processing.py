# data_processing.py

from geospatial_utils import find_nearest_stations
from api_client import get_gas_stations

def process_gas_stations_data(latitude, longitude):
    """
    Processes gas stations data by fetching nearby stations, finding the nearest ones,
    and sorting them by fuel price to find the station offering the lowest price.

    Parameters:
    - latitude: Latitude of the user's location.
    - longitude: Longitude of the user's location.

    Returns:
    - A dictionary containing details of the gas station with the lowest fuel price,
      or None if no suitable station is found.
    """
    # Fetch gas stations data from the API
    stations = get_gas_stations(latitude, longitude)

    if not stations:
        return None

    # Find the 10 nearest stations to the user's location
    nearest_stations = find_nearest_stations((latitude, longitude), stations)

    # Sort the nearest stations by fuel price (correcting the key to match the API response)
    nearest_stations_sorted_by_price = sorted(nearest_stations, key=lambda x: float(x['Precio Gasoleo A'].replace(',', '.')) if x['Precio Gasoleo A'].strip() else float('inf'))

    # Check if we have any stations left after sorting
    if not nearest_stations_sorted_by_price:
        return None

    # Select the station with the lowest fuel price
    cheapest_station = nearest_stations_sorted_by_price[0]

    # Construct the response dictionary with corrected keys
    response = {
        'name': cheapest_station.get('Rótulo', 'Unknown'),
        'address': cheapest_station.get('Dirección', 'Unknown address'),
        'price': cheapest_station.get('Precio Gasoleo A', 'N/A'),
        'latitude': cheapest_station.get('Latitud', 'N/A').replace(',', '.'),
        'longitude': cheapest_station.get('Longitud (WGS84)', 'N/A').replace(',', '.')
    }

    return response

def format_station_message(station):
    """
    Formats a message detailing the gas station with the lowest price.

    Parameters:
    - station: A dictionary containing details of the gas station.

    Returns:
    - A formatted string message.
    """
    if not station:
        return "Sorry, we couldn't find any gas station near you with available price data."

    # Construct Google Maps URL for directions
    google_maps_url = f"https://www.google.com/maps/dir/?api=1&destination={station['latitude']},{station['longitude']}"

    # Construct and return the message
    message = (f"Cheapest Gas Station:\n"
               f"Name: {station['name']}\n"
               f"Address: {station['address']}\n"
               f"Price: {station['price']} €/L\n"
               f"Directions: {google_maps_url}")

    return message
