import discord
from discord.ext import commands
import json
import random
import os

ID = ""
for i in range(3):
    ID += str(random.randrange(0, 10))
for i in range(2):
    ID += chr(random.randrange(ord("a"), ord("z"))).capitalize()
for i in range(1):
    ID += str(random.randrange(0, 10))

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

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Connected to dc")

@bot.event
async def on_message(msg):
    
    if str(msg.author) != "serverBot#4962":
        return
    
    data = get_data(DATA_FILE)
    self_data = data["self"]
    send_msg = f"{ID} = {self_data}"
    
    data.update(eval(msg.content))
    save_data(DATA_FILE, data)
    
    await msg.channel.send(send_msg)

bot.run(TOKEN)
