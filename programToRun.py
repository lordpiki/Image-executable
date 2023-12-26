import discord
from discord.ext import commands

# Function to read token and channel ID from a file
def read_tokens_from_file(file_path='tokens.token'):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        token = lines[0].strip()
        channel_id = int(lines[1].strip())
    return token, channel_id

# Get token and channel ID from the file
TOKEN, CHANNEL_ID = read_tokens_from_file()
print(TOKEN, CHANNEL_ID)

# Define intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await bot.change_presence(activity=discord.Game(name='Imagine'))
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Hello, Discord!')
    exit()

@bot.command(name='send_message')
async def send_message(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Hello, Discord!')

bot.run(TOKEN)
