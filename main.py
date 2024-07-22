import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # Permite que o bot receba eventos de mensagens

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Estou Online")
    print(bot.user.name)
    print(bot.user.id)
    print('------NN------')

#Comando de olá
@bot.event
async def on_message(message):
    if message.content.lower().startswith("Olá"):
        print("Comando 'Olá' foi utilizado")
        await message.channel.send('Olá, eu sou o Jorginho, vamos brincar na neve!')

bot.run('dEEktNDJCS54AYt59SCIZ1SoFh4jxybP')
