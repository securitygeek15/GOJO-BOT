
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
            if message.author.bot:
                return

            # Prevent counting messages that are commands
            ctx = await self.bot.get_context(message)
            if ctx.valid:
                return  # It's a command, don't count it here

            self.user_messages[message.author.id] += 1

            # Still allow command processing
            await self.bot.process_commands(message)

        except Exception as e:
            print(f"[on_message] Error: {e}")

    @commands.command()
    async def topchatters(self, ctx):
        try:
            if not self.user_messages:
                await ctx.send("No message data collected yet.")
                return

            top = sorted(self.user_messages.items(), key=lambda x: x[1], reverse=True)[:5]
            lines = []

            for user_id, count in top:
                user = ctx.guild.get_member(user_id)
                if user:
                    lines.append(f"**{user.display_name}** — {count} messages")
                else:
                    lines.append(f"**User Left** — {count} messages")

            await ctx.send("📈 **Top Chatters:**\n" + "\n".join(lines))

        except Exception as e:
            await ctx.send("An error occurred while fetching top chatters.")
            print(f"[topchatters] Error: {e}")

async def setup(bot):
    try:
        await bot.add_cog(Analytics(bot))
    except Exception as e:
        print(f"[setup] Error loading Analytics cog: {e}")
