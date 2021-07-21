import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
import keep_alive

import os

#-----SETUP-----#

prefix = "$$"

#use the .env feature to hide your token

keep_alive.keep_alive()
token = os.getenv("TOKEN")
#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

@bot.event
async def on_ready():
  activity = discord.Game(name="Iblis#1069", type=4)
  # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Iblis#1069"))
  await bot.change_presence(status=discord.Status.idle, activity=activity)
  print(f'''{Fore.RED}

 ______     __         __     __     ______     __  __     ______    
/\  __ \   /\ \       /\ \  _ \ \   /\  __ \   /\ \_\ \   /\  ___\   
\ \  __ \  \ \ \____  \ \ \/ ".\ \  \ \  __ \  \ \____ \  \ \___  \  
 \ \_\ \_\  \ \_____\  \ \__/".~\_\  \ \_\ \_\  \/\_____\  \/\_____\ 
  \/_/\/_/   \/_____/   \/_/   \/_/   \/_/\/_/   \/_____/   \/_____/ 
                                                                     
{Fore.GREEN}

 ______     __   __     __         __         __     __   __     ______    
/\  __ \   /\ "-.\ \   /\ \       /\ \       /\ \   /\ "-.\ \   /\  ___\   
\ \ \/\ \  \ \ \-.  \  \ \ \____  \ \ \____  \ \ \  \ \ \-.  \  \ \  __\   
 \ \_____\  \ \_\\"\_\  \ \_____\  \ \_____\  \ \_\  \ \_\\"\_\  \ \_____\ 
  \/_____/   \/_/ \/_/   \/_____/   \/_____/   \/_/   \/_/ \/_/   \/_____/ 
                                                                           

Your acount/bot Is now onlline!
''')

bot.run(token, bot=False)

