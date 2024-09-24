import discord
from discord.ext import commands
import os
import random
import requests 
intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def amogus(ctx):
    await ctx.send('kumala kumala kumala savesta')



@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)




organic = ['sisa makanan', 'bahan kimia' ,'daun' ,'kulit pisang' , 'sayur']
anorganic = ['kaca' , 'plastik' ,'stereofoam' , 'ban' , 'karet']


@bot.command()
async def pilih_sampah(ctx):
        await ctx.send("masukkan jenis sampah apa yang ingin kamu ketahui jenisnya:")
        nsg = await bot.wait_for("message")

        if nsg.content in organic:
            await ctx.send("buanglah ke sampah jenis organik")

        elif nsg.content in anorganic:
            await ctx.send("buanglah ke sampah jenis anorganik")

bot.run("MTI4Nzc0MjIxNTkyMTM0MDQyNg.GTnC7O.6radCRxVSHLeMLGIvamB8blKx0lA5oO1wXZdsc")


