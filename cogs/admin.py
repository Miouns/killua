import discord
from discord.ext import commands

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="clear", aliases=["cl", 'purge'])
  async def clear(self, ctx, *, amount):
    if not amount:
      return await ctx.send("Give me amount")
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Cleared {amount} Message(s)")

def setup(bot):
  bot.add_cog(General(bot))
