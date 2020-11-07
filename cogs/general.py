import discord
from discord.ext import commands

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="ping")
  async def ping(self, ctx):
    await ctx.send(f'Pong! {round(self.bot.latency*1000)}ms')
    
  @commands.command(name='avatar', aliases=["ava", "pfp", "av"], description="Get user avatar", usage="[@member]")
  async def ava(self, ctx):
    member = ctx.message.mentions[0]
    if not member:
      member = ctx.message.author
    embed = discord.Embed(title=f"{member.name}#{member.discriminator} Avatar", colour=0x37e666)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)
  


def setup(bot):
  bot.add_cog(General(bot))