#!/usr/bin/python3.6

import discord
import asyncio
import time

client = discord.Client()

async def my_background_task():
    #await client.wait_until_ready()
    await asyncio.sleep(3)
    print("sad debug statement")
    counter = 0
    channel = client.get_channel(454457353463529482)
    print(client.is_closed())
    #await asyncio.sleep(3)
    while not client.is_closed():
        if time.strftime("%H %M %S") == '02 00 00':
        	await channel.send(' https://imgur.com/gallery/emKQiF4')
        await asyncio.sleep(1)

    print("it does not work and I am sad")

@client.event
async def on_message(message):
    if message.content.startswith('s!test'):
        #await client.send_message(message.channel, 'kill me now')
        await message.channel.send('kill me now')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

print("debug 1")
client.loop.create_task(my_background_task())
print("debug 2")
client.run('NDU2MjA3MDQ3NDgyOTMzMjUx.DhGs0A.Ksf4TYVvTjPriDx1zVVtjNcpQaQ')
print("debug 3")
