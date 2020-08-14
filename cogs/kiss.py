from discord.ext import commands
import discord
import nekos


class Kiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Kiss"])
    async def kiss(self, ctx):
        if ctx.author == self.bot.user:
            embed = discord.Embed(colour=0xFBBACE)
            embed.set_image(url=nekos.img("kiss"))
            embed.set_footer(text=f"Demandé par {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.message.edit(embed=embed)


def setup(bot):
    bot.add_cog(Kiss(bot))
