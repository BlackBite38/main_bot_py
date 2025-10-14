# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
from settings import settings
import os
import requests
import asyncio

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def pru(ctx, a: str):
    await ctx.send(a*2)


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Yes, {ctx.subcommand_passed} is cool')


# @cool.command(name='bot')
# async def _bot(ctx):
#     """Is the bot cool?"""
#     await ctx.send('Yes, the bot is cool.')


print(os.listdir('images'))

@bot.command()
async def mem(ctx):
    # Obtiene todos los archivos dentro de la carpeta "images"
    images = os.listdir('images')
    # Elige una imagen aleatoria
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    # ¡Y así es como se puede sustituir el nombre del fichero desde una variable!

@bot.command()
async def nyoro(ctx):
    with open('images/nyocover.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('doggo')
async def doggo(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)



@bot.command('coin')
async def flip_coin(ctx):
    flip = random.randint(0, 2)
    if flip == 0:
        coin= "HEADS"
    else:
        coin= "TAILS"
    await ctx.send(coin)
@bot.command('smile')
async def gen_emodji(ctx):
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    emo = random.choice(emodji)
    await ctx.send(emo)

@bot.command("guess")
async def on_message(message):
    await message.channel.send('Guess a number between 1 and 10.')
    def is_correct(m):
        return m.author == message.author and m.content.isdigit()
    answer = random.randint(1, 10)
    try:
        guess = await bot.wait_for('message', check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        return await message.channel.send(f'Sorry, you took too long it was {answer}.')
    if int(guess.content) == answer:
        await message.channel.send('You are right!')
    else:
        await message.channel.send(f'Oops. It is actually {answer}.')


bot.run(settings["TOKEN"])