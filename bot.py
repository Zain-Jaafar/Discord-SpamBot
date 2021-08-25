import discord
import random
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")

@bot.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.", 
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - Definitely.",
        "You may rely on it"
        "As I see it, yes.",
        "Most Likely.",
        "Yes.",
        "Ask again later.",
        "Better not tell you.",
        "Cannot predict now",
        "Error 404, answer not found, please ask again.",
        "Don't count on it.",
        "No.",
        "My sources say no.",
        "Quite unlikely"
    ]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@bot.command()
async def beemovie(ctx):
    bee_movie_script = open("beemoviescript.txt")
    lines = bee_movie_script.readlines()
    for line in lines:
        await ctx.send(line)

@bot.command()
async def rickroll(ctx):
    rickroll_lyrics = open("rickrolllyrics.txt")
    lines = rickroll_lyrics.readlines()
    for line in lines:
        await ctx.send(line)

@bot.command()
#@commands.has_role("C")
async def spam(ctx, amount, *, thing):
    for i in range(int(amount)):
        await ctx.send(thing)
        
@bot.command()
async def spamdm(ctx, amount, member:discord.Member, *, message):
    await ctx.channel.purge(limit=1)
    for i in range(int(amount)):
        await member.send(message)

bot.run("TOKEN")
