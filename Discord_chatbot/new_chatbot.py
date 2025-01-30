import sys
import discord

# Your bot token and name here
# discordToken = ""
name = "David"  # Set your bot's name here

if discordToken == "":
    sys.exit("ERROR: Please set the Discord token.")
if name == "":
    sys.exit("ERROR: Please set the name of the bot.")

# Intents setup
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Respond to specific content without requiring a prefix or bot name
    if message.content.lower() == "hi":
        await message.channel.send("Hello! I am here to assist you.")

    elif message.content.lower() == "how are you":
        await message.channel.send("I'm just a bot, but I'm doing great! How about you?")

    elif "help" in message.content.lower():
        await message.channel.send("Sure! How can I help you today?")

# Run the bot
client.run(discordToken)