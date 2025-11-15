# AskPerplexity Discord Bot

My boyfriend and I quiz eachother on random Netflix Series, and we are chronically on Discord. I like winning debates and being able to fact check him in the middle of an argument. I got tired of having to Google some obscure plot, send him a link, and then win an argument.
So I built the AskPerplexity Bot, a simple Discord bot that integrates with Perplexity AI to answer questions directly in your Discord server.
I now win quickly. :)

Also, he proposed to me after I built this bot. Win-Win!

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
