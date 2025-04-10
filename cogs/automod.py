from discord.ext import commands
import discord

BAD_WORDS = ['badword1', 'badword2', 'badword3']
MAX_MENTIONS = 5
MAX_LINKS = 3

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        # Bad words
        if any(word in message.content.lower() for word in BAD_WORDS):
            await message.delete()
            await message.channel.send(f"🚫 {message.author.mention}, watch your language!")

        # Mention spam
        if len(message.mentions) > MAX_MENTIONS:
            await message.delete()
            await message.channel.send(f"📛 {message.author.mention}, too many mentions!")

        # Link spam
        if message.content.count("http") > MAX_LINKS:
            await message.delete()
            await message.channel.send(f"🔗 {message.author.mention}, stop spamming links!")

async def setup(bot):
    await bot.add_cog(AutoMod(bot))
