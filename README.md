# Python Telegram Bot for Gas Stations

## Project Overview
This Python Telegram Bot assists users in finding the nearest gas station with the lowest fuel price in Spain. It integrates with the Spanish public endpoint for gas stations, providing real-time data on fuel prices and station locations based on user-provided latitude and longitude.

## Features
- **Real-time Gas Station Data**: Fetches data from the Spanish public endpoint for gas stations.
- **Geospatial Calculations**: Utilizes geopy for calculating distances and finding the nearest stations.
- **Lowest Price Finder**: Identifies the cheapest gas station among the nearest ones.
- **User-friendly Bot Responses**: Formats messages with station information and Google Maps directions.
- **Robust Error Handling**: Manages errors gracefully, providing helpful feedback to the user.

## Technology Stack
- Python 3.8+
- python-telegram-bot 20.8
- requests
- geopy

## Setup and Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up your Telegram bot token in `config.py`.
4. Run `bot.py` to start the bot.

## Usage
Interact with the bot using the `/lowestprice` command followed by your latitude and longitude, e.g., `/lowestprice 40.416775 -3.703790`.

## Development Process and Prompts
The development of this bot was guided by a series of prompts, focusing on API integration, data processing, error handling, and user interaction. Key prompts included:
- Creating a bot that integrates with the Spanish public endpoint for gas stations.
- Using geopy for geospatial calculations instead of custom tools.
- Testing the endpoint and analyzing the response to ensure compatibility.
- Modifying `data_processing.py` and `geospatial_utils.py` based on findings.
- Searching the Python Telegram Bot documentation for solutions.
- Adapting the bot for version 20.8 of python-telegram-bot.

## Testing
The project includes a test suite (`test_bot.py`) covering API integration, data processing, bot responses, and error handling.

## Future Work
Future enhancements could include supporting additional commands, integrating more data sources, and improving user interaction.

## Contributing
Contributions are welcome! Please follow the standard coding conventions and submit pull requests for review.

