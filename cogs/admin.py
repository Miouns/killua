import discord
from discord.ext import commands

class Admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="clear", aliases=["cl", 'purge'])
  async def clear(self, ctx, *, amount):
    if not amount:
      return await ctx.send("Give me amount")
    await ctx.channel.purge(limit=int(amount))
    await ctx.send(f"Cleared {amount} Message(s)")

def setup(bot):
  bot.add_cog(Admin(bot))
