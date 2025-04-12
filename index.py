import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
from steam_web_api import Steam
import datetime
import os
import time
import random # Some cool imports so I have the essentials and some cool toys to play with

intents = discord.Intents(messages= True, guilds=True, typing = True, presences = True) # Discord updated their API to include this bullshit

channelId= 1158117219016900799 # General talks channel
SteamKey = "" # Steam API Key || DO NOT SHARE
steam = Steam(SteamKey)
AlxSteamID = 76561199553007835
RivalsAppID = 2767030


AlxRecentStats = steam.users.get_user_recently_played_games(AlxSteamID)

bot = commands.Bot(command_prefix= '!', intents=discord.Intents.all()) # Sets the bot prefix to !, configurable
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged on as Alx Bot!') # Console debug message
    await bot.change_presence(activity=discord.Game(name="Just big chillin'")) # Sets status, configurable
        

#This is the format for commands:

#bot.command(pass_context=True)
#async def COMMAND_NAME(ctx):
    #channel= bot.get_channel(channelId)
    #await channel.send("MESSAGE")



@bot.command(pass_context=True)
async def catchphrase(ctx):
    channel =bot.get_channel(channelId)
    if channel == "None":
        print("Holy fuck we fucked up bad")
    await channel.send("I want f*ck you money!")

@bot.command(pass_context = True)
async def fuckyoualex(ctx):
    channel= bot.get_channel(channelId)
    await channel.send(":cry:")

@bot.command(pass_context = True)
async def thatscrazy(ctx):
    channel= bot.get_channel(channelId)
    await channel.send("Whoa dawg, that's crazy")

@bot.command(pass_context = True)
async def cat(ctx):
    channel= bot.get_channel(channelId)
    await channel.send("I love my kitty, Ginger :)")
    await channel.send(file=discord.File("ginger.jpg")) # Awww

@bot.command(pass_context = True)
async def when(ctx):
    channel= bot.get_channel(channelId)
    await channel.send("When am I getting on?")
    await channel.send("Yeah for sure") # Consider integrating a pause inbetween these messages

@bot.command(pass_context = True)
async def cancer(ctx):
    channel= bot.get_channel(channelId)
    await channel.send("Breast cancer awareness is super important, dawg!") 
    await channel.send(file=discord.File("cancerawareness.jpg"))  

@bot.command(pass_context = True)
async def rolld20(ctx):
    channel= bot.get_channel(channelId)
    result = random.randint(1,20)
    final = 'You rolled a ', result,' dawg!'
    await channel.send(final) # For some reason includes the syntax in the result, I can't be bothered honestly

@bot.command(pass_context = True)
async def wyd(ctx):
    channel= bot.get_channel(channelId)
    await channel.send("What am I doing?")
    await channel.send("Well when I came home, I watched some YouTube, after that I got sleepy so I took a nap, after that, I've just been big chillin' dawg")
    await channel.send("You wanted to play games?")
    await channel.send("Dawg I've got to do my math homework")


@bot.command(pass_context = True)
async def help(ctx): # Update with all commands added
    channel= bot.get_channel(channelId)
    await channel.send("My current functioning commands are:\n!help\n!wyd\n!catchphrase\n!lookleft/!lookright\n!gimmeaminute\n!fuckyoualex\n!thatscrazy\n!cat\n!when\n!cancer\n!rolld20")

@bot.command(pass_context = True)
async def lookleft(ctx):
    channel= bot.get_channel(channelId)
    await channel.send("\*looks right\*")

@bot.command(pass_context = True)
async def lookright(ctx):
    channel= bot.get_channel(channelId)
    await channel.send("\*looks left\*")

@bot.command(pass_context = True) # Counts down from 60 but picks a random number he can't count past lmao
async def gimmeaminute(ctx):
    channel=bot.get_channel(channelId)
    result = random.randint(1,60)
    print(result)
    timer= 60
    while timer != result:
        timer -= 1
        await channel.send(timer)
    if timer != 0:
     await channel.send("I forget what comes next dawg")

@bot.command(pass_context=True)
async def rivals(ctx):
    channel = bot.get_channel(channelId)
    f= open('AlxStats.txt', 'w')
    f.write(str(AlxRecentStats))
    print("Debug")
    await channel.send(AlxRecentStats)


bot.run('') # DO NOT SHARE || API KEY