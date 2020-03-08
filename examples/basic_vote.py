import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='?', description=description)
voteString = "https://www.gtop100.com/topsites/MapleStory/sitedetails/MapleRoyals-Nostalgic-MapleStory-Server-79510?vote=1&pingUsername={}"
accountNameDict = {}

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def vote(ctx):
    await ctx.send("Click here to vote!\n" + voteString.format(accountNameDict[ctx.message.author.mention])

@bot.command()
async def register(ctx, userId : str):
    accountNameDict[ctx.message.author.mention] = userId
    await bot.say("user registered with MapleRoyals Id {}".format(ctx.message.author.mention, userId))

bot.run('token')
