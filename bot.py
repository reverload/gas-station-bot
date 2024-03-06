# bot.py

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import TELEGRAM_BOT_TOKEN, GOOGLE_MAPS_BASE_URL
from data_processing import process_gas_stations_data
import asyncio  # Added import for asyncio

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! Use /lowestprice followed by your latitude and longitude to find the lowest gas price near you.')

async def lowest_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Find and send the gas station with the lowest price near the user's location."""
    try:
        # Extract user location (latitude and longitude) from the message
        user_location = update.message.text.split()[1:]  # Expected format: /lowestprice <latitude> <longitude>
        if len(user_location) != 2:
            await update.message.reply_text('Please provide "/lowestprice" followed by your location as two numbers: latitude and longitude.')
            return

        latitude, longitude = map(float, user_location)
        # Process gas stations data to find the one with the lowest price
        cheapest_station = process_gas_stations_data(latitude, longitude)

        if cheapest_station:
            # Construct the Google Maps URL for directions
            maps_url = f"{GOOGLE_MAPS_BASE_URL}{cheapest_station['latitude']},{cheapest_station['longitude']}"
            # Construct and send the response message
            response_message = (f"Lowest Price Station: {cheapest_station['name']}\n"
                                f"Address: {cheapest_station['address']}\n"
                                f"Price: {cheapest_station['price']} €\n"
                                f"Directions: {maps_url}")
            await update.message.reply_text(response_message)
        else:
            await update.message.reply_text('No gas stations found within a reasonable distance. Try a different location.')
    except Exception as e:
        logger.error(f"Error finding the lowest price gas station: {e}")
        await update.message.reply_text('An error occurred while processing your request. Please try again.')
    

if __name__ == '__main__':
    """Start the bot."""
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # On different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("lowestprice", lowest_price))

    # Start the Bot
    application.run_polling()