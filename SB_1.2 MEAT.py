# StripeBorg_3000 Michael Kolev 18/03/2020 Version 1.2
# Optimised for Purveyors of Fine Meats Discord
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WELCOME_MESSAGE = os.getenv('STRIPE_CHECK')
emote_toep = "<:toep:686105751495901184>"
# Levens Server"<:toep:689620241197694980>"
# Meats Server "<:toep:686105751495901184>"
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# Welcome message, changed the .env file (not reccomended)
@client.event
async def on_member_join(member):
    await member.createdm()
    await member.dm_channel.send(WELCOME_MESSAGE)


# Stops bots from responding to himself.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "spriest":
        response = emote_toep
        await message.channel.send(response)
    elif message.content.lower() == "toep":
        response = emote_toep
        await message.channel.send(response)
    elif message.content.lower() == "felstriker":
        response = emote_toep
        await message.channel.send(response)
    elif message.content.lower() == "handsome":
        response = emote_toep
        await message.channel.send(response)
    elif message.content.lower() == "stripe":
        response = emote_toep
        await message.channel.send(response)
    elif message.content.lower() == "shadow":
        response = emote_toep
        await message.channel.send(response)
    elif message.content.lower() == "tfer":
        response = emote_toep
        await message.channel.send(response)
    elif message.content.lower() == "toep":
        response = emote_toep
        await message.channel.send(response)
    elif message.content == emote_toep:
        response = emote_toep
        await message.channel.send(response)
    elif message.content.lower() == "stripper":
        response = emote_toep
        await message.channel.send(response)
    # These commands send images.
    elif message.content.lower() == "?test":
        await message.channel.send(file=discord.File('test.png'))
    else:
        return


"""
# For sending images. Images must be located at the root of .py file.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "?test":
        await message.channel.send(file=discord.File('test.png'))
"""

client.run(TOKEN)
