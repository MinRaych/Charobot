from discord.ext import commands
import discord
import nekos
class Hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Hug"])
    async def hug(self, ctx):
        if ctx.author == self.bot.user:
            embed = discord.Embed(colour=0xFBBACE)
            embed.set_image(url=nekos.img("hug"))
            embed.set_footer(text=f"Demandé par {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.message.edit(embed=embed)

def setup(bot):
    bot.add_cog(Hug(bot))
