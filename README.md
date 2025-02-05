# FinalFantasy-Aerith-Discord-Bot

A simple Discord bot that fetches random images of **Aerith Gainsborough** from *Final Fantasy* using **SerpAPI** and sends them to a Discord channel.

## Features
- Retrieves random images of Aerith from **Google Images**.
- Uses **SerpAPI** for image search.
- Simple command to trigger the image search.

## Requirements
Before running the bot, make sure you have:
- Python 3.8+
- A valid **Discord Bot Token**
- A valid **SerpAPI Key**

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/FinalFantasy-Aerith-Discord-Bot.git
   cd FinalFantasy-Aerith-Discord-Bot
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   - Replace `"YOUR_DISCORD_BOT_TOKEN"` with your actual Discord bot token.
   - Replace `"YOUR_SERPAPI_KEY"` with your actual **SerpAPI** key.

## Usage
Run the bot using:
```sh
python bot.py
```

### Commands
| Command | Description |
|---------|-------------|
| `!aerith` | Fetches a random image of Aerith Gainsborough and sends it to the channel. |

## Configuration
Ensure that:
- Your bot has **message sending** permissions in the Discord server.
- Your **SerpAPI key** has enough free searches available.

## Example
User: `!aerith`  
Bot: *(Sends a random image of Aerith from Google Images)*  

## Disclaimer
This bot is for educational and entertainment purposes only. All images belong to their respective owners.  

## License
This project is licensed under the **MIT License**. See `LICENSE` for more details.
