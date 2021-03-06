import discord
from discord.ext import commands
from discord import Embed
from requests import get
import random


class Util(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    
  @commands.command(name="npm")
  async def npm(self, ctx, *, npm):
    res = get("https://registry.npmjs.com/%s" %(npm)).json()
    name = res["name"]
    desc = res["description"]
    author = res["author"]["name"]
    url = res["homepage"]
    
    embed = Embed(
      title=name, 
      color=random.choice(self.bot.color),
      description=desc,
      url=url
    )
    embed.add_field(name="Name: ", value=name, inline=False)
    embed.add_field(name="Author: ", value=author, inline=False)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Util(bot))
