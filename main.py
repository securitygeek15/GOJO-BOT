from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX", "!")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Load all cogs before running the bot
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f"Loaded cog: {filename}")
            except Exception as e:
                print(f"Failed to load cog {filename}: {e}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())
