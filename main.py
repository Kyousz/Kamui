import discord
import random

TOKEN = "ODM0NTgwMDIyODExMDMzNjIw.YIC9Nw.o8YazsHSZ-uqpgFfS-IEPu_L4LA"

client = discord.Client()

@client.event
async def on_ready():
    print("Bot ON")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".oi"):
        await message.channel.send("Oi")

    if message.content.startswith(".r"):
        await message.channel.send(random.randint(1,20))

client.run(TOKEN)