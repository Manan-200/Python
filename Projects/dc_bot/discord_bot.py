import discord
import random
import json

FILEPATH = "data.json"
with open("token.json", "r") as file:
    dict = json.load(file)
    TOKEN = dict["token"]

cmds = ["/commands", "/print", "/play"]
games = ["Guess A Number"]

def save_data(filepath, data):
    with open(filepath, "w") as file:
        json.dump(file, data)

def load_data(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return(data)
    except:
        return {}

# data = load_data(FILEPATH)
# save_data(FILEPATH, data)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

#Choosing server
@client.event
async def on_ready():
    print(f"Connected to Discord.")

#To prevent changing nickname
@client.event
async def on_member_update(_, after): 
    n = after.nick 
    if n: # Check if they updated their username
        if n.lower().count("manan") == 1:
            await after.edit(nick="knifehaver")

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")
    
    if message.author == client.user:
         return

    if user_message[0] == "/":
        for cmd in cmds:
            if cmd in user_message.lower():
                command = cmd
                txt_arr = user_message[len(command) + 1:]
                
                if cmd == cmds[0]:
                    await message.channel.send(cmds)
                    
                if cmd == cmds[1]:
                    await message.channel.send(txt_arr)
                    await message.delete()

                if cmd == cmds[2]:
                    await message.channel.send("Choose a game to play: ")
                    for game in games:
                        await message.channel.send(game)
        return

client.run(TOKEN)