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
    "“Great things never come from comfort zones.”",
    "“The only way to do great work is to love what you do.” – Steve Jobs",
    "“Success is not the key to happiness. Happiness is the key to success.” – Albert Schweitzer",
    "“Don’t watch the clock; do what it does. Keep going.” – Sam Levenson",
    "“You are never too old to set another goal or to dream a new dream.” – C.S. Lewis",
    "“Believe you can and you're halfway there.” – Theodore Roosevelt",
    "“The future belongs to those who believe in the beauty of their dreams.” – Eleanor Roosevelt",
    "“In the middle of every difficulty lies opportunity.” – Albert Einstein",
    "“It does not matter how slowly you go as long as you do not stop.” – Confucius",
    "“Everything you’ve ever wanted is on the other side of fear.” – George Addair",
    "“Opportunities don't happen, you create them.” – Chris Grosser",
    "“Dream it. Wish it. Do it.”",
    "“Success usually comes to those who are too busy to be looking for it.” – Henry David Thoreau",
    "“The only limit to our realization of tomorrow is our doubts of today.” – Franklin D. Roosevelt",
    "“You miss 100% of the shots you don’t take.” – Wayne Gretzky",
    "“I find that the harder I work, the more luck I seem to have.” – Thomas Jefferson",
    "“The way to get started is to quit talking and begin doing.” – Walt Disney",
    "“Your limitation—it’s only your imagination.”",
    "“Push yourself, because no one else is going to do it for you.”",
    "“Great things never come from comfort zones.”",
    "“Dream it. Wish it. Do it.”",
    "“Success doesn’t just find you. You have to go out and get it.”",
    "“The harder you work for something, the greater you’ll feel when you achieve it.”",
    "“Dream bigger. Do bigger.”",
    "“Don’t stop when you’re tired. Stop when you’re done.”",
    "“Wake up with determination. Go to bed with satisfaction.”",
    "“The key to success is to focus on goals, not obstacles.”",
    "“Success is the sum of small efforts, repeated day in and day out.” – Robert Collier",
    "“Don’t wait for opportunity. Create it.”",
    "“The only place where success comes before work is in the dictionary.” – Vidal Sassoon",
    "“If you can dream it, you can do it.” – Walt Disney",
    "“To be the best, you must be able to handle the worst.”",
    "“Hardships often prepare ordinary people for an extraordinary destiny.” – C.S. Lewis",
    "“Don’t limit your challenges. Challenge your limits.”",
    "“If you’re not willing to risk the usual, you will have to settle for the ordinary.” – Jim Rohn",
    "“The future depends on what we do in the present.” – Mahatma Gandhi",
    "“The secret of getting ahead is getting started.” – Mark Twain",
    "“It’s not whether you get knocked down, it’s whether you get up.” – Vince Lombardi",
    "“If you can’t fly, then run. If you can’t run, then walk. If you can’t walk, then crawl, but whatever you do, you have to keep moving forward.” – Martin Luther King Jr.",
    "“We may encounter many defeats, but we must not be defeated.” – Maya Angelou",
    "“You don’t have to be great to start, but you have to start to be great.” – Zig Ziglar",
    "“The road to success and the road to failure are almost exactly the same.” – Colin R. Davis",
    "“Success is walking from failure to failure with no loss of enthusiasm.” – Winston Churchill",
    "“I never lose. I either win or learn.” – Nelson Mandela",
    "“A winner is a dreamer who never gives up.” – Nelson Mandela",
    "“Don’t wait for the perfect moment. Take the moment and make it perfect.”",
    "“The best time to plant a tree was 20 years ago. The second best time is now.” – Chinese Proverb",
    "“You only live once, but if you do it right, once is enough.” – Mae West",
    "“Success is not final, failure is not fatal: It is the courage to continue that counts.” – Winston Churchill",
    "“Success is not how high you have climbed, but how you make a positive difference to the world.” – Roy T. Bennett",
    "“Do what you can with all you have, wherever you are.” – Theodore Roosevelt",
    "“What you get by achieving your goals is not as important as what you become by achieving your goals.” – Zig Ziglar",
    "“Your time is limited, don’t waste it living someone else’s life.” – Steve Jobs",
    "“You only live once, but if you do it right, once is enough.” – Mae West",
    "“In the end, we only regret the chances we didn’t take.”",
    "“Hard work beats talent when talent doesn’t work hard.”",
    "“It always seems impossible until it’s done.” – Nelson Mandela",
    "“Keep your face always toward the sunshine—and shadows will fall behind you.” – Walt Whitman",
    "“We cannot solve our problems with the same thinking we used when we created them.” – Albert Einstein",
    "“If you want to achieve greatness stop asking for permission.”",
    "“Everything you can imagine is real.” – Pablo Picasso",
    "“Do one thing every day that scares you.” – Eleanor Roosevelt",
    "“Success is not in what you have, but who you are.”",
    "“The journey of a thousand miles begins with one step.” – Lao Tzu",
    "“Doubt kills more dreams than failure ever will.” – Suzy Kassem",
    "“Everything has beauty, but not everyone can see it.” – Confucius",
    "“Be the change that you wish to see in the world.” – Mahatma Gandhi",
    "“I am not a product of my circumstances. I am a product of my decisions.” – Stephen R. Covey",
    "“Your life does not get better by chance, it gets better by change.” – Jim Rohn",
    "“Act as if what you do makes a difference. It does.” – William James",
    "“Success is not the absence of failure; it’s the persistence through failure.” – Aisha Tyler",
    "“The only limit to our realization of tomorrow is our doubts of today.” – Franklin D. Roosevelt",
    "“Life is what happens when you’re busy making other plans.” – John Lennon"
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
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    "I used to play piano by ear, but now I use my hands.",
    "What’s orange and sounds like a parrot? A carrot.",
    "What do you call a belt made of watches? A waist of time!",
    "I couldn't figure out how to put my seatbelt on. Then it clicked.",
    "Why don’t oysters share their pearls? Because they’re shellfish.",
    "Why was the math book sad? It had too many problems.",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "How does a penguin build its house? Igloos it together.",
    "Why was the computer cold? It left its Windows open.",
    "I told my computer I needed a break, and it froze.",
    "What do you call a fish wearing a bowtie? Sofishticated.",
    "Why was the broom late? It swept in.",
    "Why don’t you ever see elephants hiding in trees? Because they’re really, really good at it.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "What’s a skeleton’s least favorite room? The living room.",
    "What do you call a group of musical whales? An orca-stra.",
    "Why can’t you trust an atom? Because they make up everything.",
    "I told my wife she should embrace her mistakes. She gave me a hug.",
    "Why can’t you hear a pterodactyl go to the bathroom? Because the ‘P’ is silent.",
    "I used to play piano by ear, but now I use my hands.",
    "What’s a skeleton’s least favorite room? The living room.",
    "What do you call a bear with no teeth? A gummy bear.",
    "How do cows stay up to date with current events? They read the moo-s paper.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "What do you call a pile of cats? A meow-tain.",
    "What’s a vampire’s favorite fruit? A *blood* orange.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "Why did the math book look sad? Because it had too many problems.",
    "What do you call an alligator in a vest? An investigator!",
    "I couldn’t figure out why I couldn’t get any work done on my laptop. Turns out, I had too many windows open.",
    "Why don’t sharks like fast food? Because they can’t catch it.",
    "What do you call fake spaghetti? An *impasta*.",
    "What did the grape do when it got stepped on? Nothing but let out a little wine.",
    "How do you organize a space party? You planet.",
    "Why don’t you ever see hippos hiding in trees? Because they’re really good at it.",
    "What’s a vampire’s favorite fruit? A *blood* orange.",
    "What do you call a fish without eyes? Fsh.",
    "Why did the belt go to jail? Because it was holding up a pair of pants!",
    "What do you get when you cross a snowman and a dog? Frostbite.",
    "I was wondering why the frisbee kept getting bigger, but then it hit me.",
    "What do you call a pile of kittens? A meow-tain.",
    "How does a penguin build its house? Igloos it together.",
    "What do you call an elephant that doesn’t matter? An irrelephant.",
    "I asked the librarian if the library had any books on paranoia. She whispered, ‘They’re right behind you.’",
    "What’s brown and sticky? A stick.",
    "What do you call a dinosaur with an extensive vocabulary? A thesaurus.",
    "Why do cows have hooves instead of feet? Because they lactose.",
    "I wasn’t originally going to get a brain transplant, but then I changed my mind.",
    "What do you call a fish with no eyes? Fsh.",
    "What’s black and white and red all over? A sunburned zebra.",
    "Why did the chicken join a band? Because it had the drumsticks.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "What do you call a sheep with no legs? A cloud.",
    "What do you get when you cross a snowman with a dog? Frostbite.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "What’s orange and sounds like a parrot? A carrot.",
    "What do you call a group of musical whales? An orca-stra.",
    "What do you call an alligator in a vest? An investigator!",
    "What’s a skeleton’s least favorite room? The living room.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why was the computer cold? It left its Windows open.",
    "Why can’t you trust an atom? Because they make up everything."
]

        await ctx.send(random.choice(jokes))

    @commands.command()
    async def roast(self, ctx):
        roasts = [
    "You bring everyone so much joy… when you leave the room.",
    "If I had a dollar for every smart thing you said, I’d be broke.",
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "I would agree with you, but then we’d both be wrong.",
    "You have the perfect face for radio.",
    "If ignorance is bliss, you must be the happiest person alive.",
    "I’ve seen salads dressed better than you.",
    "You're proof that even a broken clock is right twice a day.",
    "You're not stupid; you just have bad luck thinking.",
    "You have the right to remain silent because whatever you say will probably be stupid.",
    "I’m not saying I hate you, but I would unplug your life support to charge my phone.",
    "You are like a software update. Whenever I see you, I think, 'Not now.'",
    "If I wanted to hear from an idiot, I’d just talk to myself.",
    "You’re like a phone with no signal, always out of touch.",
    "You’re the human equivalent of a participation trophy.",
    "It’s not that you’re ugly, you’re just... not very good looking.",
    "You bring everyone so much happiness when you leave the room.",
    "I would explain it to you, but I left my English-to-Dingbat dictionary at home.",
    "You’ve got the perfect face for radio.",
    "If I had a nickel for every time you said something intelligent, I’d be broke.",
    "You have an entire life to be a jerk. Why not take today off?",
    "I’m not saying I hate you, but I’d unplug your life support to charge my phone.",
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "Your secrets are always safe with me. I never even listen when you tell me them.",
    "Your brain is like a web browser: too many tabs open, and none of them are helpful.",
    "I’d agree with you, but then we’d both be wrong.",
    "You’re like a software update; you take too long and nobody asked for you.",
    "Your soul is so dark, I need sunglasses just to look at you.",
    "You're proof that evolution can go in reverse.",
    "You're not the sharpest tool in the shed, but you’re definitely the rustiest.",
    "I'd explain it to you, but I left my English-to-Dingbat dictionary at home.",
    "You’re like a phone with no signal: useless.",
    "You make a rock look like a rocket scientist.",
    "I’ve seen vegetables smarter than you.",
    "If I had a brain, I’d be dangerous... but you have one and you still manage to be dumb.",
    "If I wanted to listen to an idiot, I’d talk to myself.",
    "You must be the square root of negative one… because you’re imaginary.",
    "You’re like a cloud. You disappear when you’re most needed."
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
            result = f"It's a tie! We both chose {bot_choice}."
        elif (user == "rock" and bot_choice == "scissors") or (user == "paper" and bot_choice == "rock") or (user == "scissors" and bot_choice == "paper"):
            result = f"You win! I chose {bot_choice}."
        else:
            result = f"You lose! I chose {bot_choice}."

        await ctx.send(result)

async def setup(bot):
    await bot.add_cog(Fun(bot))
