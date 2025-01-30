import sys
# This is mainly taken from https://discordpy.readthedocs.io/en/stable/quickstart.html
# To make the file watch for changes (the script is restarted each time you save the file),
# npm package nodemon can be used:
# 1: Install npm if you do not have it yet:
#    sudo apt update
#    sudo apt install npm
# 2. To install nodemon: sudo npm i -g nodemon
# 3: To run the file: nodemon --exec python3 bottemplate.py

# discordToken = "" # Your bot token here (https://discord.com/developers/applications/ and tab Bot -> Token -> Reset Token -> Copy the token here)
name = "" # Your bot name here


if (discordToken == ""): sys.exit("ERROR: Please set the discord token.")
if (name == ""): sys.exit("ERROR: Please set the name of the bot.")

# To use this package, install: pip3 install discord.py
import discord # type: ignore

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message : discord.message.Message):
  if message.author == client.user: return # We don't want to reply to ourselves

  # RULE: To not flood the channel with responses from multiple bots,
  # we only respond to messages that start with our name

  if message.content.startswith(name):
    print(f"{message.author} says: {message.content}")

    if message.content.startswith(f'{name} Hi'):
      await message.channel.send('I have joined into the server.')

client.run(discordToken)
