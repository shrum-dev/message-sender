import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
async def announce(ctx, *, message):
    if ctx.author.id == 1085538596955627580:
        await ctx.message.delete()
        await ctx.send("||@everyone||")
        embed = discord.Embed(
            description=message,
            color=0x98ce0d
        )
        embed.set_image(url='https://media.discordapp.net/attachments/1086656323837513769/1086656384520704071/excer.png?width=1440&height=301')
        await ctx.send(embed=embed)

bot.run('your_token')
