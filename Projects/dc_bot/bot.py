import discord
from discord import app_commands
from discord.ext import commands
import json

with open("token.json", "r") as f:
    TOKEN = json.load(f)["token"]

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

@bot.tree.command(name="print")
@app_commands.describe(msg = "what should I say?")
async def print_msg(interaction: discord.Interaction, msg:str):
    await interaction.response.send_message(f"{msg}")

@bot.tree.command(name="games")
async def games(interaction: discord.Interaction):
    await interaction.response.send_message("game1, game2, game3")

bot.run(TOKEN)