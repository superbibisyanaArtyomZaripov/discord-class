import discord
import random
import os
import requests 
from discord.ext import commands
from model import detect_cat
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import DepthwiseConv2D
from keras import layers
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет Я бот!{bot.user}')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def minus(ctx, left: int, right: int):
    """minus"""
    await ctx.send(left - right)
@bot.command()
async def x(ctx, left: int, right: int):
    "X"
    await ctx.send(left * right)
@bot.command()
async def divide(ctx, left: int, right: int):
    "/"
    await  ctx.send(left / right)
@bot.command()
async def rc(ctx):
    rcl = random.randint(1,100)
    await ctx.send(rcl)
@bot.command()
async def helps(ctx):
    await ctx.send("команда x умножает два числа команда divide делит два числа команда add плюсует два числа команда minus минусует два числа команда choose выбирает из разных строк команда rc выбирает рандомное число от 1 до 100 команда nickname дает новое имя на сервере команда еcology рассказывает рандомный факт про экологию musor сколько он разлогается(мусор) а ecomeme присылает мем с экологией")
@bot.command()
async def nickname(ctx, nickname : str):
    await ctx.send(f"{ctx.author.mention}, твой ник изменен на {nickname} !")
    await ctx.author.edit(nick=nickname)
@bot.command()
async def mem(ctx):
    s =os.listdir('images')
    img_name = random.choice(s)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
@bot.command()
async def cats(ctx):
    c = os.listdir('animals')
    cats = random.choice(c)
    with open(f'animals/{cats}', 'rb') as f:
        pictur = discord.File(f)
        await ctx.send(file=pictur)

@bot.command()
async def ecology(ctx):
    ecologyfacts = ["В Тихом океане есть мусорное пятно, площадь которого достигает 1,5 млн км², что больше площади большинства стран мира. Течения сносят сюда миллионы тонн мусора ежегодно, и он превратился в подобие мусорного континента"," В Австралии экологические организации натягивают искусственные лианы над автодорогами, чтобы коалы не рисковали погибнуть, перебегая эти дороги.","Половина населения Земли пьёт воду, загрязнённую в той или иной степени, а потому небезопасную для здоровья","Ежегодно на Земле высаживается лишь около 10% деревьев от того их числа, которое вырубается за тот же срок.","Около 15% всех смертей и смертельных заболеваний в мире вызвано высоким уровнем загрязнения воздуха.","Чистые пруды в Москве ещё в недавнем прошлом были так загрязены, что назывались Погаными."]
    rfacts = random.choice(ecologyfacts)
    await ctx.send(rfacts)
@bot.command()
async def musor(ctx):
    musor = ["батарейки разлагаются около 110 лет","пластик разлогается не меньше 180-200 лет","фольга разлагается более 100 лет","железная арматура разлагается около 11-13 лет","консервная банка разлогается 10 лет"]
    rmusor = random.choice(musor)
    await ctx.send(rmusor)
@bot.command()
async def ecomeme(ctx):
    ecomem = os.listdir('ecology')
    randomecology = random.choice(ecomem)
    with open(f'ecology/{randomecology}', 'rb') as f:
        ememe = discord.File(f)
        await ctx.send(file=ememe)
@bot.command()
async def check(ctx):
       attachments =  ctx.message.attachments
       if attachments:
            for attachment in attachments:
                file_name = attachment.filename
                file_url  =  attachment.url
                await attachment.save(f'savepics/{file_name}')
                
                cat = detect_cat(f"images/{file_name}")
                await ctx.send(f"на картинке изображено {cat}")
                name = detect_cat({cat})
                if name == 'сфинкс':
                    await ctx.send("это сфинкс, лысая пародия кота,его кормят     нежирную телятину, курятину, перемороженную и обработанную кипятком;некоторые субпродукты;морскую рыбу и морепродукты;овощи;овсяную, рисовую кашу без соли;яичные желтки.")
                if name == 'сиамский':
                    await ctx.send("НЕ ВЕДИСЬ это кот сделанный с помощью ИИ это обман")

       else:
           await ctx.send("вы забыли загрузить картинку")

    



bot.run('token')


