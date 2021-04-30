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
async def oi(ctx):
    if ctx.author.id == 235490465342816256:
        await ctx.send(f"Oi amiga {ctx.author.mention}!")
    else:
        await ctx.send("Você não é minha amiga!")

@client.command()
async def r(ctx, num:str, mod:int=0):
    soma = []
    crit = []
    x = (num.split("+"))
    for n in range(0,len(x)):
        dado, valor = (int(a) for a in x[n].split("d"))
        rolagens = [random.randint(1, valor) for i in range(dado)]
        soma.extend(rolagens)
        for j in range(0,len(rolagens)):
            if rolagens [j] == valor:
                crit.append(f"**{rolagens[j]}**")
            elif rolagens [j] == 1:
                crit.append(f"**{rolagens[j]}**")
            else:
                crit.append(rolagens[j])
        result = " + ".join([str(r) for r in crit])
    if mod > 0:
        simb = (f"+ {mod}")
    elif mod < 0:
        simb = (f"- {mod*(-1)}")
    else:
        simb = ""
    await ctx.send(f"🎲 ***Rolagem de {ctx.author.mention}***"
                   f"\n**Resultado**: {num} ({result}) {simb}"
                   f"\n**Total**: {sum(soma)+mod}")

@client.command()
async def d(ctx, min, max):
    resultado = random.randint(int(min),int(max))
    await ctx.send(f"🎲 ***Rolagem de Dano: {ctx.author.mention}***"
                   f"\n**Poder de Ataque**: {min} ~ {max} "
                   f"\n**Resultado**: {resultado}")

client.run(TOKEN)