import discord
from discord.ext import commands
from requests import get

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(name="8ball", aliases=["8b"])
  async def _8ball(self, ctx, *, question):
    answer = get(url="https://nekos.life/api/v2/8ball").json()
    await ctx.send("> %s\n%s %s" %(question, ctx.author.mention, answer["response"]))
    


def setup(bot):
  bot.add_cog(Fun(bot))