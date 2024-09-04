# Telegram Channel Word Counter

This script analyzes messages in a Telegram channel and counts word frequency. It uses the [Telethon library](https://github.com/LonamiWebs/Telethon) to interact with the Telegram API.
<img src="https://raw.githubusercontent.com/wakeoneself/telecount/main/telecount_demo.gif" width="500" alt="Demo of the application">
## Features

- Count word frequency in a specified Telegram channel
- Ability to specify the number of messages to analyze
- Ignore short words (configurable minimum length)
- Use of .env file for storing sensitive data

## Requirements

- Python 3.7+
- Libraries: telethon, python-dotenv

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/wakeoneself/telecount.git
   cd telecount
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # For Unix or MacOS
   venv\Scripts\activate  # For Windows
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a .env file in the root directory of the project and add your data:
   ```
   API_ID=your_api_id
   API_HASH=your_api_hash
   PHONE_NUMBER=your_phone_number
   ```

   You can obtain API_ID and API_HASH from https://my.telegram.org

## Usage

Run the script by specifying the channel username (without the @ symbol) and the number of messages to analyze:

```
python telecount.py channelname 1000
```

This will analyze the last 1000 messages in the "channelname" channel.

## Notes

- You may need to go through the Telegram authentication process on the first run.
- The script ignores words shorter than 3 letters (this value can be changed in the code).
- Results are output to the console as the top 20 most frequently used words.

## Security

- Never pass your API_ID, API_HASH, and phone number directly in the code.
- Make sure the .env file is added to .gitignore to avoid accidentally publishing your sensitive data.

## License

This project is distributed under the MIT license. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.