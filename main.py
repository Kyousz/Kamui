import discord
import random

TOKEN = "ODM0NTgwMDIyODExMDMzNjIw.YIC9Nw.o8YazsHSZ-uqpgFfS-IEPu_L4LA"
prefix = "."
client = discord.Client()
# args = message.content.slice(prefix.length).trim().split( / + / g)
# command = args.shift().toLowerCase()

@client.event
async def on_ready():
    print("Bot Online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".oi"):
        await message.channel.send("Bom dia")

    if message.content.startswith(".r"):
        await message.channel.send(random.randint(1,20))

client.run(TOKEN)