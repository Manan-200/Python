import discord
from discord import app_commands
from discord.ext import commands
import json
import random

DATA_FILE = "num_guess.json"

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
game1_data = data_dict["g1"]

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
async def hello(interaction:discord.Interaction):  
    await interaction.response.send_message(f"hey mf")

@bot.tree.command(name="print_data")
async def print_msg(interaction:discord.Interaction):
    await interaction.response.send_message(f"{game1_data}")

@bot.tree.command(name="games")
async def games(interaction:discord.Interaction):
    await interaction.response.send_message("num_guess, game2, game3")

@bot.tree.command(name="ping")
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message("pong!")

@bot.tree.command(name="embed")
async def embed(interaction:discord.Interaction, member:discord.Member=None):
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

@bot.tree.command(name="generate_num")
async def generate_num(interaction:discord.Interaction):
    await interaction.response.send_message("Random number has been generated between 1 and 50!")
    game1_data["state"] = True
    game1_data["num"] = random.randrange(1, 51)
    game1_data["lives"] = 5
    save_data(DATA_FILE, game1_data)

@bot.tree.command(name="guess")
async def guess(interaction:discord.Interaction, num:int):
    if game1_data["state"]:
        if game1_data["num"] == num:
            await interaction.response.send_message("You guessed the correct number")
            await interaction.response.send_message("gg")
            game1_data["state"] = False
        else:
            if game1_data["num"] < num:
                await interaction.response.send_message("Your guess is too big")
            elif game1_data["num"] > num:
                await interaction.response.send_message("Your guess is too small")
            game1_data["lives"] -= 1
            if game1_data["lives"] == 0:
                await interaction.response.send_message("You lost")
                game1_data["state"] = False
    else:
        await interaction.response.send_message("First use /generate_num")
    
bot.run(TOKEN)
