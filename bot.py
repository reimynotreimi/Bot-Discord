import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(',say'):
        
        content = message.content[len(',say'):].strip()
        await message.channel.send(content)
        
        await message.delete()

client.run('token')
