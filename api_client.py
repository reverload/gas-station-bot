# api_client.py

import requests
from config import GAS_STATION_API_ENDPOINT
from error_handling import handle_api_error

def get_gas_stations(latitude, longitude):
    """
    Fetches gas stations data from the Spanish public endpoint using the provided latitude and longitude.
    Returns a list of gas stations with their details or an empty list if an error occurs or no data is found.
    """
    try:
        # Construct the full URL with parameters for latitude and longitude
        full_url = f"{GAS_STATION_API_ENDPOINT}estacionesTerrestres?latitud={latitude}&longitud={longitude}"
        
        # Make the HTTP GET request to the API
        response = requests.get(full_url)
        
        # Check if the response status code indicates success (200 OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Check if the data contains the expected list of gas stations
            if 'ListaEESSPrecio' in data:
                return data['ListaEESSPrecio']
            else:
                # If the expected data is not found, log or handle accordingly
                handle_api_error("Expected data 'ListaEESSPrecio' not found in API response.")
                return []
        else:
            # If the response status code is not 200, log or handle the error
            handle_api_error(f"API request failed with status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        # Handle any exceptions raised during the request
        handle_api_error(f"An error occurred while making the API request: {e}")
        return []

