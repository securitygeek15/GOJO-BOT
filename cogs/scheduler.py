from discord.ext import commands, tasks
import discord
import datetime

class Scheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def schedule(self, ctx, time: str, *, msg: str):
        # Basic HH:MM parsing
        target_time = datetime.datetime.strptime(time, "%H:%M").time()
        await ctx.send(f"⏰ Message scheduled at {time} - I'll remind you!")

        @tasks.loop(seconds=60)
        async def check_and_send():
            now = datetime.datetime.now().time()
            if now.hour == target_time.hour and now.minute == target_time.minute:
                await ctx.send(f"⏰ Reminder: {msg}")
                check_and_send.stop()

        check_and_send.start()

async def setup(bot):
    await bot.add_cog(Scheduler(bot))


