# AskPerplexity Discord Bot

My boyfriend and I are chronically online, and our Discord chats are basically 90% Netflix references, meme quotes, Instagram reels, and random YouTuber dialogues. The problem? We're constantly trying to remember who said what, which episode it's from, or where that one specific meme came from.
Our conversations kept going like this:

_Me: *drops obscure reference_

_Him: "Wait, what's that from again?"_

_Me: *frantically Googling while he keeps texting_
_Me: scrolling through 47 Reddit threads trying to find it_

_Me: finally sends link_

_Him: has already moved on to a completely different topic_

I just wanted to share references and actually explain them in the moment, without killing the vibe of our conversation, you know?
So I built the AskPerplexity Bot, a Discord bot that integrates with Perplexity AI to instantly answer questions right in our chat.
Now we can explain references as fast as we make them, relive our favorite moments together, and keep the conversation flowing without those awkward Google breaks. 

***Also, he proposed to me after I built this bot. Causal or Corelated? Dunno, but its a win-win!***

<img width="1071" height="546" alt="Screenshot 2025-11-14 at 8 10 06 PM" src="https://github.com/user-attachments/assets/aac5bc5c-0da0-415b-922c-22828c11827d" />


## Features

- Ask Perplexity AI questions using `!ask <question>`
- Real-time web search capabilities
- Handles long responses by splitting them into multiple messages
- Simple and easy to set up

<img width="1020" height="320" alt="Screenshot 2025-11-14 at 7 41 05 PM" src="https://github.com/user-attachments/assets/f8dbbbff-8603-48d9-a6eb-4b219e557b58" />


## Setup Instructions

### 1. Get Your API Keys

**Discord Bot Token:**
1. Go to https://discord.com/developers/applications
2. Click "New Application" and give it a name
3. Go to the "Bot" section in the left sidebar
4. Click "Add Bot"
5. Under "Token", click "Reset Token" and copy it (you'll need this)
6. Enable "MESSAGE CONTENT INTENT" under "Privileged Gateway Intents"
7. Go to "OAuth2" > "URL Generator"
8. Select scopes: `bot`
9. Select bot permissions: `Send Messages`, `Read Messages/View Channels`, `Read Message History`
10. Copy the generated URL and open it in your browser to invite the bot to your server

**Perplexity API Key:**
1. Go to https://www.perplexity.ai/settings/api
2. Sign up or log in
3. Generate a new API key
4. Copy the API key

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Edit `.env` and add your tokens:
```
DISCORD_TOKEN=your_actual_discord_token
PERPLEXITY_API_KEY=your_actual_perplexity_key
```

### 4. Run the Bot

```bash
python perplexity-discord-bot.py
```

You should see: `<BotName> has connected to Discord!`

## Usage

In any Discord channel where the bot has access:

```
!ask What is the capital of France?
!ask Explain machine learning in simple terms
!ask What are the latest news about AI?
!help_perplexity
```

## Customization

- **Change the command prefix:** Edit `command_prefix='!'` in the bot setup
- **Change the model:** Modify the `model` parameter in the API call. This project uses 'sonar'

## Troubleshooting

- **Bot doesn't respond:** Make sure "MESSAGE CONTENT INTENT" is enabled in Discord Developer Portal
- **API errors:** Check that your Perplexity API key is valid and has credits
- **Permission errors:** Ensure the bot has "Send Messages" permission in the channel

## Notes

- Perplexity API is a paid service. Check pricing at https://docs.perplexity.ai/docs/pricing
- The bot uses the online model which includes web search capabilities
- Discord messages are limited to 2000 characters; long responses are automatically split

## License

MIT
