import discord
from discord.ext import commands
import json
import os

with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config["PREFIX"], intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config["TOKEN"])
