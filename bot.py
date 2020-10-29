import discord
from discord.ext import commands
import os
import jishaku

bot = commands.AutoShardedBot(
  command_prefix="k!",
  shard_count=3,
  owner_ids=[681843628317868049, 593774699654283265]
  )

bot.load_extension("jishaku")

@bot.command(name="hello")
async def hello(ctx):
  await ctx.send("Hello");

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(os.environ["SECRET"])