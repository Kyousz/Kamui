import discord
from discord.ext import commands
import random

TOKEN = "ODM0NTgwMDIyODExMDMzNjIw.YIC9Nw.o8YazsHSZ-uqpgFfS-IEPu_L4LA"

client = commands.Bot(command_prefix = ".", case_insensitive = True)

@client.event
async def on_ready():
    print("{0.user.name} está online!".format(client))
    await client.change_presence(activity=discord.Game(name="RPG | .ajuda"))

@client.command()
async def ajuda(ctx):
    embed=discord.Embed(
        title="LISTA DE COMANDOS",
        description="Todos os comandos de Kamui!",
        color=discord.Color.purple())
    embed.set_author(name="Kyous ~ O Criador", icon_url="https://pbs.twimg.com/profile_images/1336294229270736898/6bpP84te_400x400.jpg")
    embed.add_field(name="**.r [dados] [mod]**",
                    value="Rolar um ou mais dados com mesma quantidade de lados somando ou diminuindo modificadores.", inline=False)
    embed.add_field(name="**.d [danoMIN] [danoMAX]**",
                    value="Rolar o dano de uma arma ou magia acrescentando apenas o dano mínimo e o máximo.", inline=False)
    embed.set_footer(text="Versão: 1.2")
    await ctx.send(embed=embed)

@client.command()
async def metas(ctx):
    await ctx.send("- Fazer rolagens como: 1d20+1d6+2"
                   "\n- Deixar números máximos e mínimos em destaque.")

@client.command()
async def r(ctx, num:str="", mod:int=0):
    lista = []
    x = (num.split("+"))
    for n in range(0,len(x)):
        dado, valor = (int(a) for a in x[n].split("d"))
        rolagens = [random.randint(1, valor) for i in range(dado)]
        lista.extend(rolagens)
        result = " + ".join([str(r) for r in lista])
    simb = "+" if mod > 0 else ""
    await ctx.send(f"🎲 ***Rolagem de {ctx.author.mention}***"
                   f"\n**Resultado**: {num} ({result}) {simb} {mod}"
                   f"\n**Total**: {sum(lista)+mod}")

@client.command()
async def d(ctx, min, max):
    resultado = random.randint(int(min),int(max))
    await ctx.send(f"🎲 ***Rolagem de Dano: {ctx.author.mention}***"
                   f"\n**Min/Max**: {min} ~ {max} "
                   f"\n**Resultado**: {resultado}")

client.run(TOKEN)