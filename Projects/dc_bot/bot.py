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

bot.run(TOKEN)
