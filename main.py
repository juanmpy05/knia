import discord
import asyncio
import config
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
prefix = 'z!'
bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), intents=intents, application_id=config.APPLICATION_ID)

@bot.event
async def on_ready():
    activity = discord.Game(name='Bot bug dance', type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print('logged on as', bot.user)

@bot.event
async def on_message(message):

    # Primero procese los eventos
    if message.content.startswith(prefix):
        await bot.process_commands(message) 

    # don't respond to ourselves
    elif message.author == bot.user:
        return
    
    elif message.content == 'ping':
        await message.channel.send('Pong.')

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())