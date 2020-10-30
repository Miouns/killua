import discord
from discord.ext import commands
from asyncio import sleep

class Admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="clear", aliases=["cl", 'purge'])
  async def clear(self, ctx, *, amount):
    if not amount:
      return await ctx.send("Give me amount")
    await ctx.channel.purge(limit=int(amount))
    msg = await ctx.send(f"<a:tick:769242226349572136> Cleared {amount} Messages")
    await sleep(5.0)
    await msg.delete()

def setup(bot):
  bot.add_cog(Admin(bot))
