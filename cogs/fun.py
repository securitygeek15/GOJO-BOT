from discord.ext import commands
import discord
import random
import requests

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        quotes = [
            "“The best way to get started is to quit talking and begin doing.” – Walt Disney",
            "“Don't let yesterday take up too much of today.” – Will Rogers",
            "“Push yourself, because no one else is going to do it for you.”",
            "“Sometimes later becomes never. Do it now.”",
            "“Great things never come from comfort zones.”"
        ]
        await ctx.send("📢 Here's a quote:\n" + random.choice(quotes))

    @commands.command()
    async def meme(self, ctx):
        try:
            response = requests.get("https://meme-api.com/gimme").json()
            embed = discord.Embed(title=response["title"], url=response["postLink"], color=discord.Color.random())
            embed.set_image(url=response["url"])
            embed.set_footer(text=f"👍 {response['ups']} | r/{response['subreddit']}")
            await ctx.send(embed=embed)
        except:
            await ctx.send("❌ Couldn't fetch meme.")

    @commands.command()
    async def joke(self, ctx):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why do we tell actors to break a leg? Because every play has a cast!",
            "What do you call fake spaghetti? An *impasta*."
        ]
        await ctx.send(random.choice(jokes))

    @commands.command()
    async def roast(self, ctx):
        roasts = [
            "You bring everyone so much joy… when you leave the room.",
            "If I had a dollar for every smart thing you said, I’d be broke.",
            "You're like a cloud. When you disappear, it's a beautiful day."
        ]
        await ctx.send(random.choice(roasts))

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(f"{message}")

    @commands.command()
    async def eightball(self, ctx, *, question):
        responses = [
            "Yes.", "No.", "Absolutely!", "Definitely not.", "Maybe.", "Ask again later."
        ]
        await ctx.send(f"🎱 Question: {question}\nAnswer: {random.choice(responses)}")

    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send(f"The coin landed on: **{random.choice(['Heads', 'Tails'])}**")

    @commands.command()
    async def rps(self, ctx, choice: str):
        user = choice.lower()
        bot_choice = random.choice(["rock", "paper", "scissors"])
        result = ""
        if user == bot_choice:
            result = "It's a tie!"
        elif (user == "rock" and bot_choice == "scissors") or (user == "paper" and bot_choice == "rock") or (user == "scissors" and bot_choice == "paper"):
            result = "You win!"
        elif user in ["rock", "paper", "scissors"]:
            result = "I win!"
        else:
            await ctx.send("❌ Choose rock, paper, or scissors.")
            return
        await ctx.send(f"You chose **{user}**. I chose **{bot_choice}**. {result}")

async def setup(bot):
    await bot.add_cog(Fun(bot))
