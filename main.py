import discord
from discord.ext import commands
import random

TOKEN = "ODM0NTgwMDIyODExMDMzNjIw.YIC9Nw.o8YazsHSZ-uqpgFfS-IEPu_L4LA"

client = commands.Bot(command_prefix=".", case_insensitive=True)

@client.event
async def on_ready():
  print('O BOT {0.user} está online!' .format(client))

@client.command()
async def ola(ctx):
  await ctx.send(f'Olá, {ctx.author}')

@client.command()
async def r(ctx, numero1, numero2):
  variavel = random.randint(int(numero1),int(numero2))
  await ctx.send(f'O número que saiu no dado é {variavel}')

client.run(TOKEN)