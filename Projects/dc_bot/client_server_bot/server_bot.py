import discord
from discord.ext import commands
import json
import os

DATA_FILE = "data.json"

def get_data(FILE):
    try:
        with open(FILE, "r") as file:
            data = json.load(file)
        return (data)
    except:
        return {}

def save_data(FILE, data):
    with open(FILE, "w") as file:
        json.dump(data, file)

TOKEN = get_data("token.json")
data = {}
save_data(DATA_FILE, data)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Connected to dc")

@bot.event
async def on_message(msg):

    if msg.author == bot.user:
        return
        
    content = msg.content
    
    if msg.content == "send_data":
        await msg.channel.send(data)
        
    if "=" not in msg.content:
        return
    
    for seperator in range(len(content)):
        if content[seperator] == "=":
            
            client_id = content[:seperator]
            client_data = eval(content[seperator + 1:])
            
            try:
                data[client_id]["pos"] = client_data["pos"]
            except:
                data[client_id] = {}
                data[client_id]["pos"] = client_data["pos"]
                
            print(data)
            
            sending_data = {}
            for key in data:
                if key != client_id:
                    sending_data[key] = data[key]
                    
            await msg.channel.send(sending_data)
            
    save_data(DATA_FILE, data)

bot.run(TOKEN)
