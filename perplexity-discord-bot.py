import discord
from discord.ext import commands
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds')

@bot.command(name='ask')
async def ask_perplexity(ctx, *, question: str):
    """Ask Perplexity AI a question"""
    
    # Send a "thinking" message
    thinking_msg = await ctx.send(f"🤔 Searching for: *{question}*...")
    
    try:
        async with aiohttp.ClientSession() as session:
            headers = {
                'Authorization': f'Bearer {PERPLEXITY_API_KEY}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'model': 'sonar',
                'messages': [
                    {
                        'role': 'system',
                        'content': 'You are a helpful assistant. Be concise and clear.'
                    },
                    {
                        'role': 'user',
                        'content': question
                    }
                ]
            }
            
            async with session.post(
                'https://api.perplexity.ai/chat/completions',
                headers=headers,
                json=payload
            ) as response:
                
                if response.status == 200:
                    data = await response.json()
                    answer = data['choices'][0]['message']['content']
                    
                    # Discord has a 2000 character limit per message
                    if len(answer) > 1900:
                        # Split into chunks
                        chunks = [answer[i:i+1900] for i in range(0, len(answer), 1900)]
                        await thinking_msg.delete()
                        await ctx.send(f"**Question:** {question}\n\n**Answer:**")
                        for chunk in chunks:
                            await ctx.send(chunk)
                    else:
                        await thinking_msg.edit(content=f"**Question:** {question}\n\n**Answer:**\n{answer}")
                else:
                    error_text = await response.text()
                    await thinking_msg.edit(content=f"❌ Error: API returned status {response.status}\n{error_text}")
                    
    except Exception as e:
        await thinking_msg.edit(content=f"❌ Error: {str(e)}")

@bot.command(name='help_perplexity')
async def help_command(ctx):
    """Show help message"""
    help_text = """
    **Perplexity Discord Bot Commands:**
    
    `!ask <your question>` - Ask Perplexity AI anything
    `!help_perplexity` - Show this help message
    
    **Example:**
    `!ask What is the weather in San Francisco?`
    `!ask Explain quantum computing in simple terms`
    """
    await ctx.send(help_text)

if __name__ == '__main__':
    if not PERPLEXITY_API_KEY or not DISCORD_TOKEN:
        print("Error: Missing API keys. Please set PERPLEXITY_API_KEY and DISCORD_TOKEN in .env file")
    else:
        bot.run(DISCORD_TOKEN)
