
from discord.ext import commands
import discord
from collections import defaultdict

class Analytics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_messages = defaultdict(int)

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            # Skip bot messages
            if not message.author.bot:
                self.user_messages[message.author.id] += 1
            await self.bot.process_commands(message)
        except Exception as e:
            # Log error to console; in production, you might want to use a logging framework
            print(f"Error in on_message: {e}")

    @commands.command()
    async def topchatters(self, ctx):
        try:
            # Get top 5 chatters
            top = sorted(self.user_messages.items(), key=lambda x: x[1], reverse=True)[:5]
            lines = []
            for user_id, count in top:
                user = ctx.guild.get_member(user_id)
                if user:
                    lines.append(f"**{user.display_name}** — {count} messages")
                else:
                    lines.append(f"**User Left** — {count} messages")
            await ctx.send("📈 Top Chatters:\n" + "\n".join(lines))
        except Exception as e:
            await ctx.send("An error occurred while trying to retrieve the top chatters.")
            print(f"Error in topchatters command: {e}")

async def setup(bot):
    await bot.add_cog(Analytics(bot))
