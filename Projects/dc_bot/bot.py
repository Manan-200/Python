import discord
from discord import app_commands
from discord.ext import commands
import json
import random

DATA_FILE = "data.json"

def get_data(FILE):
    try:
        with open(FILE, "r") as file:
            data = json.load(file)
        return(data)
    except:
        return {}

def save_data(FILE, data):
    with open(FILE, "w") as file:
        json.dump(data, file)

TOKEN = get_data("token.json")["token"]
data_dict = get_data(DATA_FILE)

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print (f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print (e)

@bot.tree.command(name="hey")   
async def hello(interaction: discord.Interaction):  
    await interaction.response.send_message(f"hey mf")

@bot.tree.command(name="print_data")
async def print_msg(interaction: discord.Interaction):
    await interaction.response.send_message(f"{data_dict}")

@bot.tree.command(name="games")
async def games(interaction: discord.Interaction):
    await interaction.response.send_message("num_guess, game2, game3")

@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong!")

@bot.tree.command(name="embed")
async def embed(interaction: discord.Interaction, member:discord.Member = None):
    if member == None:
        member = interaction.user
    
    name = member.display_name
    pfp = member.display_avatar

    embed = discord.Embed(title=f"{name} you suck", description=f"{name} sucks", colour=discord.Colour.random())
    embed.set_author (name=f'{name}')
    embed.set_thumbnail(url=f"{pfp}")
    embed.add_field(name=f"{name} is a disgrace!", value=f"{name} is fatherless!")
    embed.set_footer(text=f"{interaction.user} created this embed!")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="num_guess")
async def num_guess(interaction: discord.Interaction):
    await interaction.response.send_message("Random number has been generated between 1 and 50!")
    num = random.randrange(1, 51)
    lives = 5
    data_dict["num"] = num
    data_dict["lives"] = lives
    save_data(DATA_FILE, data_dict)

bot.run(TOKEN)
