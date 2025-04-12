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
    "“Don’t let yesterday take up too much of today.” – Will Rogers",
    "“Push yourself, because no one else is going to do it for you.”",
    "“Sometimes later becomes never. Do it now.”",
    "“Great things never come from comfort zones.”",
    "“Dream it. Wish it. Do it.”",
    "“Success doesn’t just find you. You have to go out and get it.”",
    "“The harder you work for something, the greater you’ll feel when you achieve it.”",
    "“Don’t wait for opportunity. Create it.”",
    "“Your limitation—it’s only your imagination.”"
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
    "What do you call fake spaghetti? An *impasta*.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "How does a penguin build its house? Igloos it together.",
    "Why was the math book sad? Because it had too many problems.",
    "Why can’t your nose be 12 inches long? Because then it would be a foot.",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "I told my computer I needed a break, and it said 'No problem, I’ll crash.'",
    "Parallel lines have so much in common… it’s a shame they’ll never meet."
]

        await ctx.send(random.choice(jokes))

    @commands.command()
    async def roast(self, ctx):
        roasts = [
                "You bring everyone so much joy… when you leave the room.",
                "If I had a dollar for every smart thing you said, I’d be broke.",
                "You're like a cloud. When you disappear, it's a beautiful day.",
            "You have something on your chin... no, the third one down.",
            "You're not stupid — you just have bad luck thinking.",
            "You have something on your face... oh wait, that's just your face.",
            "You're proof that even evolution takes breaks.",
            "You're like a software update: I ignore you until you're impossible to avoid.",
            "You're as useful as the 'ueue' in 'queue'.",
            "You're not the dumbest person alive, but you better hope they don't die."
        ]

        await ctx.send(random.choice(roasts))

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(f"{message}")

    @commands.command()
    async def eightball(self, ctx, *, question):
        responses = [
            "Yes.", "No.", "Absolutely!", "Definitely not.",
            "Maybe.", "Ask again later.", "Without a doubt.",
            "Don't count on it.", "Most likely.", "Better not tell you now.",
            "Signs point to yes.", "Very doubtful.", "Yes – definitely.",
            "Concentrate and ask again.", "Outlook not so good."
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
