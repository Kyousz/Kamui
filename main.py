import discord
from discord.ext import commands
import random

TOKEN = "ODM0NTgwMDIyODExMDMzNjIw.YIC9Nw.o8YazsHSZ-uqpgFfS-IEPu_L4LA"

client = commands.Bot(command_prefix = ".", case_insensitive = True)

@client.event
async def on_ready():
  print("{0.user.name} está online!".format(client))

@client.command()
async def ajuda(ctx):
    embed=discord.Embed(
        title="LISTA DE COMANDOS",
        description="Todos os comandos de Kamui!",
        color=discord.Color.purple())
    embed.set_author(name="Kyous", url="https://twitter.com/_Kyousz",
                     icon_url="https://pbs.twimg.com/profile_images/1336294229270736898/6bpP84te_400x400.jpg")
    embed.add_field(name="**.r [dado] [mod]**",
                    value="Rolar um ou mais dados com mesma quantidade de lados somando ou diminuindo modificadores.", inline=False)
    embed.add_field(name="**.d [danoMIN] [danoMAX]**",
                    value="Rolar o dano de uma arma ou magia acrescentando apenas o dano mínimo e o máximo.", inline=False)
    embed.set_footer(text="Versão: 1.0")
    await ctx.send(embed=embed)

@client.command()
async def r(ctx, num: str, mod: int=0):
  dado, valor = (int(texto) for texto in num.split("d"))
  rolls = [random.randint(1, valor) for i in range(dado)]
  result = " + ".join([str(r) for r in rolls])
  simb = "+" if mod > 0 else ""
  await ctx.send(f"🎲 ***Rolagem de {ctx.author.mention}***"
                 f"\n**Resultado**: {result} **({simb}{mod})**"
                 f"\n**Total**: {sum(rolls)+mod}")

@client.command()
async def d(ctx, min, max):
  resultado = random.randint(int(min),int(max))
  await ctx.send(f"🎲 ***Rolagem de Dano: {ctx.author.mention}***"
                 f"\n**Min/Max**: {min} ~ {max} "
                 f"\n**Resultado**: {resultado}")

client.run(TOKEN)