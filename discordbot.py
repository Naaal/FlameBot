import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Shut up you low elo trash')

client.run('')
