import discord
import weather

TOKEN = 'NjUyNzg3MzM0NzM5Mzk0NTcw.XethsA.4WnEz0YpX9BvwdrxiylzjhWFj_4'

client = discord.Client()

@client.event
async def on_ready():
    print("logged in as " + client.user.name)

@client.event
async def on_message(message):
    #botからのメッセージをはじく
    if message.author.bot:
        return
    
    #メンションして挨拶
    if message.content == 'Hi':
        target = message.author.mention
        await message.channel.send(target + 'Hi')

    #TRPG
    if  message.content == '!weather':
        weather()

client.run(TOKEN)

