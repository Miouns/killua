import discord
from discord.ext import commands
import os


bot = commands.AutoShardedBot(command_prefix="k!")

@bot.event
async def on_message(msg):
  if msg.content == "k!hello":
    mes = "Hello, {0.author.mention}".format(msg)
    await bot.send_message(msg.channel, mes)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(os.environ["SECRET"])