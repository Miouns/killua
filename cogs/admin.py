import discord
from discord.ext import commands
from asyncio import sleep
import json

class Admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="clear", aliases=["cl", 'purge'])
  @commands.has_permissions(administrator=True)
  async def clear(self, ctx, *, amount):
    if not amount:
      return await ctx.send("Give me amount")
    await ctx.channel.purge(limit=int(amount))
    msg = await ctx.send(f"<a:tick:769242226349572136> Cleared {amount} Messages")
    await sleep(5.0)
    await msg.delete()
  
  @commands.command(name="prefix", aliases=["ch", "changeprefix"])
  @commands.has_permissions(administrator=True)
  async def prefix(self, ctx, *, prefix):
    with open("../config/prefixes.json", "r") as f:
      data = json.load(f)
      
    data[str(ctx.guild.id)] = prefix
    
    with open("../config/prefixes.json", "w") as f:
      json.dump(data, f, indent=4)
    
    await ctx.send("Prefix set to `%s`" %(Prefix))

def setup(bot):
  bot.add_cog(Admin(bot))
