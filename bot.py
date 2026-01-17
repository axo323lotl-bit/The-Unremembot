import discord

# 1. Configure Intents
# This tells Discord your bot needs permission to read message content
intents = discord.Intents.default()
intents.message_content = True 

# 2. Initialize the Bot Client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # This runs when the bot successfully connects to Discord
    print(f'Successfully logged in as {client.user}')

@client.event
async def on_message(message):
    # 3. Safety Check
    # Prevents the bot from responding to its own "meep!" 
    if message.author == client.user:
        return

    # 4. The Logic
    # We use .lower() so it catches "Meep!", "MEEP!", and "meep!"
    if message.content.lower() == 'meep!':
        await message.channel.send('meep!')

# 5. Connect the Bot
# Paste your token between the quotes below

client.run('MTQ2MjEwOTA2NzIyODA4NjQ5NQ.GqsyH8.Tya-4zSs9FQnwK4TYSbEE2lzkIIGgSVvlJjnP0')
