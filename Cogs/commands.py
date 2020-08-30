import discord
from discord.ext import commands
import asyncio

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def информация(self, ctx):
        author = ctx.message.author
        e = discord.Embed(title = '**Информация о боте**', color = discord.Color.from_rgb(255, 00, 00))
        e.add_field(name = 'Бот создан специально для сервера:', value = 'Children of FREEDOM')
        e.add_field(name = '/мут', value = 'Мут участника (через час снимается)')
        e.add_field(name = '/очистить', value = 'Чистит чат')
        e.set_footer(text = f'Помощь запросил {author.name}')
        await ctx.send('', embed = e)
    
    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def мут(self, ctx, member: discord.Member):
        mute = discord.utils.get(ctx.message.guild.roles, name = 'Muted')
        e = discord.Embed(title = member.name + ' был замучен на 1 час', color = discord.Color.from_rgb(00, 255, 00))
        await ctx.send('', embed = e)
        await member.add_roles(mute)
        await asyncio.sleep(3600)
        await member.remove_roles(mute)
    
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def очистить(self, ctx, amount = 1):
        author = ctx.message.author
        await ctx.channel.purge(limit = amount)
        await ctx.send(f'{author.mention} очистил чат', delete_after = 4)



def setup(bot):
    bot.add_cog(Commands(bot))