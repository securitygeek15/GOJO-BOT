from discord.ext import commands
import discord

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        if channel:
            await channel.send(f"👋 Welcome {member.mention} to {member.guild.name}!")

        role = discord.utils.get(member.guild.roles, name="Member")
        if role:
            await member.add_roles(role)

async def setup(bot):
    await bot.add_cog(Welcome(bot))
