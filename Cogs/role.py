import discord
import asyncio
from discord.ext import commands

class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def stopdropandroll(self, ctx):
        await ctx.message.delete()
        role = discord.utils.get(ctx.message.guild.roles, name = 'Разноцветный динамический')
        while True:
            await role.edit(color = discord.Color.from_rgb(1, 00, 00))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(255, 00, 00))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(00, 255, 00))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(00, 00, 255))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(254, 255, 255))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(102, 00, 255))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(204, 00, 102))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(00, 153, 204))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(204, 204, 00))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(153, 00, 255))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(00, 255, 102))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(35, 13, 33))
            await asyncio.sleep(90)
            await role.edit(color = discord.Color.from_rgb(255, 215, 00))
            await asyncio.sleep(90)


def setup(bot):
    bot.add_cog(Role(bot))