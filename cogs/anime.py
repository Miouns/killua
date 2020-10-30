import discord
from discord.ext import commands
from jikanpy import Jikan
from discord import Embed

jikan = Jikan()

class Anime(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(name="anime", aliases=["searchanime"])
  async def anime(self, ctx, *, anime):
    anime = jikan.search("anime", str(anime), page=1)
    result = anime["results"][0]
    title = result["title"]
    image = result["image_url"]
    desc = result["synopsis"]
    episodes = result["episodes"]
    rate = result["rate"]
    created = result["start_date"]
    status = result["end_date"]
    
    star = ":star:"*round(rate)
    
    if status:
      status = "ended"
    else:
      status = "ongoing"
    embed = Embed(
      title=title,
      description=desc
      colour=0x03fc35
      )
    embed.add_field(name="Title: ", value=title, inline=False)
    embed.add_field(name="Rate: ", value=f'{star}/{rate}', inline=False)
    embed.add_field(name="Status: ", value=status)
    embed.add_field(name="Episodes: ", value=episodes)
    embed.set_thumbnail(url=image)
    

def setup(bot):
  bot.add_cog(Anime(bot))