# Telegram Channel Word Counter

This script analyzes messages in a Telegram channel and counts word frequency. It uses the [Telethon library](https://github.com/LonamiWebs/Telethon) to interact with the Telegram API.

<text-center>
<img src="https://raw.githubusercontent.com/wakeoneself/telecount/main/telecount_demo.gif" width="600" alt="Demo of the application"/>
</text-center>

## Features

- Count word frequency in a specified Telegram channel
- Ability to specify the number of messages to analyze
- Configurable minimum word length to ignore short words
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

Run the script by specifying the channel username (without the @ symbol), the number of messages to analyze, and optionally, the minimum word length:

```
python telecount.py channelname 1000 [--min-length MIN_LENGTH]
```

- `channelname`: The username of the Telegram channel to analyze (without the @ symbol)
- `1000`: The number of messages to analyze
- `--min-length`: (Optional) The minimum length of words to consider. Default is 3 if not specified.

Examples:

1. Analyze 1000 messages, considering words of 3 or more characters (default):
   ```
   python telecount.py channelname 1000
   ```

2. Analyze 500 messages, considering words of 4 or more characters:
   ```
   python telecount.py channelname 500 --min-length 4
   ```

This will analyze the specified number of messages in the "channelname" channel and output the top 20 most frequently used words that meet the minimum length requirement.

## Notes

- You may need to go through the Telegram authentication process on the first run.
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