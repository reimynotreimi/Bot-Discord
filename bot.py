import discord
from discord.ext import commands
import asyncio

# Intents necesarios
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Prefijo para los comandos
bot = commands.Bot(command_prefix=',', intents=intents)

# Evento para cuando el bot esté listo
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Comando ,say para repetir un mensaje y eliminar el mensaje original
@bot.command()
async def say(ctx, *, content: str):
    await ctx.send(content)
    await ctx.message.delete()

# Comando para banear usuarios por ID
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user_id: int, *, reason=None):
    user = await bot.fetch_user(user_id)
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f'{user.name} ha sido baneado por {reason}')

# Comando para crear una encuesta simple
@bot.command()
async def poll(ctx, *, question):
    message = await ctx.send(f"📊 **Encuesta**: {question}")
    await message.add_reaction("👍")
    await message.add_reaction("👎")

# Evento para dar la bienvenida a nuevos miembros
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(f"¡Bienvenido {member.mention} al servidor!")

# Comando para crear un recordatorio
@bot.command()
async def remind(ctx, time: int, *, reminder):
    await ctx.send(f"Te recordaré en {time} segundos: {reminder}")
    await asyncio.sleep(time)
    await ctx.send(f"{ctx.author.mention}, recordatorio: {reminder}")

# Elimina el comando help predeterminado
bot.remove_command('help')

# Comando personalizado de ayuda
@bot.command()
async def help(ctx):
    help_message = """
    **Comandos Disponibles**:
    `,say <mensaje>`: El bot repite el mensaje.
    `,ban <ID> [razón]`: Banea a un usuario por su ID del servidor.
    `,poll <pregunta>`: Crea una encuesta simple con reacciones 👍 y 👎.
    `,remind <segundos> <recordatorio>`: Crea un recordatorio en segundos.
    """
    await ctx.send(help_message)

# Ejecuta el bot
bot.run('tu-token-aqui')
