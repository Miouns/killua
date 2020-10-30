import discord
from discord.ext import commands

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="ping")
  async def ping(self, ctx):
    await ctx.send(f'Pong! {round(self.bot.latency*1000)}')
  


def setup(bot):
  bot.add_cog(General(bot))
