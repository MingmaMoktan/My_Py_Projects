import sys
import random
import discord 


# discordToken = ""
name = ""

if (discordToken == ""): sys.exit("ERROR: Please set the discord token.")
if (name == ""): sys.exit("ERROR: Please set the name of the bot.")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message : discord.message.Message):
    if message.author == client.user: return # This code is executed here becuause We don't want to reply to ourselves
    # RULE: To not flood the channel with responses from multiple bots,
    # we only respond to messages that start with our name

    if message.content.startswith(name):
        print(f"{message.author} says: {message.content}")

        msg = message.content[len(name):].strip()
        print(f"msg contains: {msg}")
        
        # Checking if the msg starts with 'hello'
        if message.content.startswith(f"{name} Hello"):
            await message.channel.send('Welcome to mychat bot.')
            return
        msg_list = msg.split()
        
        # 1.1 Chatbot generating random number
        if msg_list[0].lower()=="random":
            if len(msg_list) == 3:
                if msg_list[1].isdigit() and msg_list[2].isdigit():
                    min_num = int(msg_list[1])
                    max_num = int(msg_list[2])
                    if min_num > max_num:
                        min_num, max_num = max_num, min_num
                    random_num = random.randint(min_num, max_num)
                    await message.channel.send(f'Random number: {random_num}')
                    return
                else:
                    await message.channel.send('Exterminate! Only digits are allowed')
                return
        # 1.2 Chatbot generating improved random number
            elif len(msg_list)==4:
                min_num = int(msg_list[1])
                max_num = int(msg_list[2])
                how_many = int(msg_list[3])
                if min_num > max_num:
                    min_num, max_num = max_num, min_num
                random_num = [random.randint(min_num, max_num) for _ in range(how_many)]            
                await message.channel.send(f'Random number: {random_num}')
                return
            elif len(msg_list)>4:
                await message.channel.send('Exterminate too many parameters.')
                return 
            else:
                await message.channel.send('Exterminate too less parameters.')
                return
        
        # 1.3 checking if the msg starts with 'sum' and gives the sum of two numbers.  
        if msg_list[0].lower()=="sum":
            if len(msg_list) == 3:
                if msg_list[1].isdigit() and msg_list[2].isdigit():
                    num_1 = int(msg_list[1])
                    num_2 = int(msg_list[2])
                    sum = num_1 + num_2
                    await message.channel.send(f'The sum of {num_1} and {num_2} number is: {sum}')
                    return
                else:
                  await message.channel.send('Exterminate! Only digits are allowed')
                  return
            elif len(msg_list)>3:
                await message.channel.send('Exterminate too many parameters.')
                return
            else:
                await message.channel.send('Exterminate too less parameters.')
                return
                       
        # 1.4 If the chat bot asks for the 'help' then gives the instructions for how to use them
        if msg.lower() == 'help':
            await message.channel.send("""Available commands:
                    1. Type hello
                  2. Type random <min> <max> and generate random numbers
                3. Type random <min> <max> <how many> and generate random numbers for the last parameter you typed.
              4. Type sum <num_1> <num_2> and generate the sum of two num_1 and num_2 is result.
                    How to use commands:
                    - Type the command followed by required parameters
                  - For example: 'random 1 10' generates 1 random numbers between 1 and 10
                - For example: 'random 1 10 3' generates 3 random numbers between 1 and 10
              - For example: 'sum 1 10' generates sum of numbers 1 and 10 and returns 11""")
            return
        elif msg.lower() == 'exit':
            await message.channel.send('Goodbye! Thank you for using the chatbot.')
            return  
        else:
            await message.channel.send("I'm sorry, I don't understand that command. Type 'help' for a list of available commands.")
            return                    
            
client.run(discordToken)