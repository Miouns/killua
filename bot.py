import discord
from discord.ext import commands
import os
import jishaku
import json
from config.colors import color, colors

async def get_prefix(bot, msg):
  with open("./config/prefixes.json", "r") as f:
    prefixes = json.load(f)
  return prefixes[str(msg.guild.id)]


bot = commands.AutoShardedBot(
  command_prefix=get_prefix,
  owner_ids=[681843628317868049, 593774699654283265]
  )

bot.colors = colors
bot.color = color

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

@bot.event
async def on_guild_join(guild):
  with open("./config/prefixes.json", "r") as f:
    prefixes = json.load(f)
    
  prefixes[str(guild.id)] = "k!"
    
  with open("./config/prefixes.json", "w") as f:
    json.dump(prefixes, f, indent=4)


@bot.event
async def on_guild_remove(guild):
  with open("./config/prefixes.json", "r") as f:
    prefixes = json.load(f)
    
  prefixes.pop(str(guild.id))
    
  with open("./config/prefixes.json", "w") as f:
    json.dump(prefixes, f, indent=4)


for name in os.listdir('./cogs'):
  if name.endswith('.py'):
    bot.load_extension(f'cogs.{name[:-3]}')

bot.run(os.environ["SECRET"])
