# config.py

# This file contains the configuration settings for the Telegram bot and the API integration.

# Telegram Bot Token
# Replace 'YOUR_TELEGRAM_BOT_TOKEN_HERE' with your actual Telegram bot token received from BotFather
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'

# API Endpoint for the Spanish public gas stations
# This is the base URL for making requests to the gas station data
GAS_STATION_API_ENDPOINT = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/'

# Google Maps Base URL
# This URL is used to generate directions to the gas station in the bot's response
GOOGLE_MAPS_BASE_URL = 'https://www.google.com/maps/dir/?api=1&destination='

# Maximum Distance
# This defines the maximum distance (in kilometers) to search for gas stations from the user's location
MAX_DISTANCE_KM = 50

# Number of Stations to Consider
# This defines how many of the nearest stations to consider when looking for the lowest price
NUM_STATIONS_CONSIDER = 10
