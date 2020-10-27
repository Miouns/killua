import discord
from discord.ext import commands
import os


bot = commands.AutoShardedBot(command_prefix="k!")

@commands.command(name="hello")
async def hello(ctx):
  await ctx.send("Hello");

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(os.environ["SECRET"])