import asyncio
import logging
import re
from collections import Counter
import argparse
from telethon import TelegramClient
from telethon.tl.types import InputPeerChannel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Disable Telethon's logs for connection
logging.getLogger('telethon.network').setLevel(logging.WARNING)
logging.getLogger('telethon.client.telegrambaseclient').setLevel(logging.WARNING)

# Get data from environment variables
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')

# Check for necessary environment variables
if not all([api_id, api_hash, phone_number]):
    logger.error("Missing required environment variables. Make sure the .env file contains API_ID, API_HASH, and PHONE_NUMBER.")
    exit(1)

# Minimum word length to consider
MIN_WORD_LENGTH = 3

# Regular expression for matching words in multiple languages
WORD_REGEX = re.compile(r'\b[\w-]+\b', re.UNICODE)

async def count_words(client, channel, limit):
    word_counter = Counter()
    message_count = 0

    async for message in client.iter_messages(channel, limit=limit):
        if message.text:
            words = [word.lower() for word in WORD_REGEX.findall(message.text) if len(word) >= MIN_WORD_LENGTH]
            word_counter.update(words)
            message_count += 1

        if message_count % 100 == 0:
            logger.info(f"Processed messages: {message_count}")

    logger.info(f"Total messages processed: {message_count}")
    return word_counter

async def main(channel_username, post_limit):
    async with TelegramClient('session', api_id, api_hash) as client:
        logger.info("Connecting to Telegram...")
        await client.start(phone=phone_number)
        logger.info("Connected successfully")

        logger.info(f"Retrieving channel information: {channel_username}")
        channel = await client.get_entity(channel_username)
        
        logger.info(f"Starting to parse channel: {channel_username}")
        logger.info(f"Number of posts to analyze: {post_limit}")

        word_counts = await count_words(client, channel, post_limit)

        logger.info("Parsing completed. Outputting results.")
        print(f"\nTop 20 most frequently used words (minimum {MIN_WORD_LENGTH} letters):")
        for word, count in word_counts.most_common(20):
            print(f"{word}: {count}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parser for counting words in a Telegram channel")
    parser.add_argument("channel", help="Channel username to analyze (without @ symbol)")
    parser.add_argument("limit", type=int, help="Number of posts to analyze")
    args = parser.parse_args()

    asyncio.run(main(args.channel, args.limit))