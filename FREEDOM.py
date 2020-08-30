import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix = '/')
bot.remove_command('help')

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

@bot.event
async def on_ready(guild = discord.Guild):
    await bot.change_presence(activity = discord.Game('/информация'))
    while True:

        wlc = bot.get_channel(710750292693614622)
        cht = bot.get_channel(710169413701074986)
        spm = bot.get_channel(716239689954099201)
        mus = bot.get_channel(710450845786832937)
        ide = bot.get_channel(713438925473054781)
        rul = bot.get_channel(710456746333962262)
        par = bot.get_channel(710818771811696680)
        mem = bot.get_channel(710941456919166988)
        slo = bot.get_channel(712232106092396565)
        zhl = bot.get_channel(748166462350557244)
        sti = bot.get_channel(748166809248858232)
        que = bot.get_channel(749587705670664302)
        spk = bot.get_channel(710169413701074988)
        muz = bot.get_channel(710450807857872949)
        tal = bot.get_channel(721034760553627708)
        prv = bot.get_channel(724258850856894615)

        await wlc.edit(name = '«🚇»метро')
        await cht.edit(name = '«💬»общий-чат')
        await spm.edit(name = '«🚭»курилка')
        await mus.edit(name = '«🎶»музыка')
        await ide.edit(name = '«🤔»идеи')
        await rul.edit(name = '«❗»правила')
        await par.edit(name = '«🤝»партнёрства')
        await mem.edit(name = '«😂»мемы')
        await tal.edit(name = '«💠»байки')
        await slo.edit(name = '«🍌»слова')
        await zhl.edit(name = '«🤬»жалобы')
        await sti.edit(name = '«📗»стихи')
        await que.edit(name = '«❓»квесты')
        await spk.edit(name = '«🔉»Основной')
        await muz.edit(name = '«🎧»Музыка')
        await prv.edit(name = '«🗣»Приват')

        await asyncio.sleep(7200)

        await wlc.edit(name = '❬🚇❭метро')
        await cht.edit(name = '❬💬❭общий-чат')
        await spm.edit(name = '❬🚭❭курилка')
        await mus.edit(name = '❬🎶❭музыка')
        await ide.edit(name = '❬🤔❭идеи')
        await rul.edit(name = '❬❗❭правила')
        await par.edit(name = '❬🤝❭партнёрства')
        await mem.edit(name = '❬😂❭мемы')
        await tal.edit(name = '❬💠❭байки')
        await slo.edit(name = '❬🍌❭слова')
        await zhl.edit(name = '❬🤬❭жалобы')
        await sti.edit(name='❬📗❭стихи')
        await que.edit(name='❬❓❭квесты')
        await spk.edit(name = '❬🔉❭Основной')
        await muz.edit(name = '❬🎧❭Музыка')
        await prv.edit(name = '❬🗣❭Приват')

        await asyncio.sleep(7200)

        await wlc.edit(name = '꧁🚇꧂метро')
        await cht.edit(name = '꧁💬꧂общий-чат')
        await spm.edit(name = '꧁🚭꧂курилка')
        await mus.edit(name = '꧁🎶꧂музыка')
        await ide.edit(name = '꧁🤔꧂идеи')
        await rul.edit(name = '꧁❗꧂правила')
        await par.edit(name = '꧁🤝꧂партнёрства')
        await mem.edit(name = '꧁😂꧂мемы')
        await tal.edit(name = '꧁💠꧂байки')
        await slo.edit(name = '꧁🍌꧂слова')
        await zhl.edit(name = '꧁🤬꧂жалобы')
        await sti.edit(name='꧁📗꧂стихи')
        await que.edit(name='꧁❓꧂квесты')
        await spk.edit(name = '꧁🔉꧂Основной')
        await muz.edit(name = '꧁🎧꧂Музыка')
        await prv.edit(name = '꧁🗣꧂Приват')

        await asyncio.sleep(7200)

        await wlc.edit(name = '≻🚇метро')
        await cht.edit(name = '≻💬общий-чат')
        await spm.edit(name = '≻🚭курилка')
        await mus.edit(name = '≻🎶музыка')
        await ide.edit(name = '≻🤔идеи')
        await rul.edit(name = '≻❗правила')
        await par.edit(name = '≻🤝партнёрства')
        await mem.edit(name = '≻😂мемы')
        await tal.edit(name = '≻💠байки')
        await slo.edit(name = '≻🍌слова')
        await zhl.edit(name = '≻🤬жалобы')
        await sti.edit(name='≻📗стихи')
        await que.edit(name='≻❓квесты')
        await spk.edit(name = '≻🔉Основной')
        await muz.edit(name = '≻🎧Музыка')
        await prv.edit(name = '≻🗣Приват')

        await asyncio.sleep(7200)

        await wlc.edit(name = '❲🚇❳метро')
        await cht.edit(name = '❲💬❳общий-чат')
        await spm.edit(name = '❲🚭❳курилка')
        await mus.edit(name = '❲🎶❳музыка')
        await ide.edit(name = '❲🤔❳идеи')
        await rul.edit(name = '❲❗❳правила')
        await par.edit(name = '❲🤝❳партнёрства')
        await mem.edit(name = '❲😂❳мемы')
        await tal.edit(name = '❲💠❳байки')
        await slo.edit(name = '❲🍌❳слова')
        await zhl.edit(name = '❲🤬❳жалобы')
        await sti.edit(name='❲📗❳стихи')
        await que.edit(name='❲❓❳квесты')
        await spk.edit(name = '❲🔉❳Основной')
        await muz.edit(name = '❲🎧❳Музыка')
        await prv.edit(name = '❲🗣❳Приват')

        await asyncio.sleep(7200)

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel.id == 724258850856894615:
        for guild in bot.guilds:
            if guild.id == 710169413202214925:
                mainCategory = discord.utils.get(guild.categories, id = 710169413701074985)
                channel2 = await guild.create_voice_channel(name = f'{member.display_name}', category = mainCategory)
                await member.move_to(channel2)
                await channel2.set_permissions(member, manage_channels = True)

                def check(a, b, c):
                    return len(channel2.members) == 0
                
                await bot.wait_for('voice_state_update', check = check)
                await channel2.delete()

bot.run('NzE4MDQ3OTY5ODM1ODc2NDAz.Xtjn2A.iMRksuA7bisuATUQtimotoJbaxo')