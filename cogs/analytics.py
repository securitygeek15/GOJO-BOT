from discord.ext import commands
import discord
from collections import defaultdict

class Analytics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_messages = defaultdict(int)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            self.user_messages[message.author.id] += 1

    @commands.command()
    async def topchatters(self, ctx):
        top = sorted(self.user_messages.items(), key=lambda x: x[1], reverse=True)[:5]
        lines = []
        for user_id, count in top:
            user = ctx.guild.get_member(user_id)
            lines.append(f"**{user.display_name}** — {count} messages")
        await ctx.send("📈 Top Chatters:\n" + "\n".join(lines))

async def setup(bot):
    await bot.add_cog(Analytics(bot))
