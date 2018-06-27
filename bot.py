#!/usr/bin/python3.6

import discord
import asyncio
import time
import random
from os import listdir
from os.path import isfile, join

images = [f for f in listdir('images') if isfile(join('images', f))]

client = discord.Client()

async def timed_message():
    #await client.wait_until_ready()
    await asyncio.sleep(3)
    print("sad debug statement")
    channel = client.get_channel(443094449233592327)
    print(client.is_closed())
    #await asyncio.sleep(3)
    while not client.is_closed():
        if time.strftime("%H %M %S") == '02 00 00':
            await channel.send('@here https://imgur.com/gallery/emKQiF4')
        await asyncio.sleep(1)

    print("it does not work and I am sad")

@client.event
async def on_message(message):
    if not message.author.bot: #man's not bot
        if message.content == 's!role':
            if time.strftime("%H") > "02" and time.strftime("%H") < "05":
                await message.channel.send("fine, here's your fucking role")
                sad_role = channel = discord.utils.get(message.guild.roles, name='sad niggas')
                await message.author.add_roles(sad_role)
            else:
                await message.channel.send("it isn't real sad nigga hours, you fucking poser")

        if message.content.split(' ', 2)[0] == 's!remind':
            rawtime = message.content.split(' ', 2)[1]
            h, m, s = rawtime.split(':')
            sectime = float(h)*3600 + float(m)*60 + float(s)
            remindtime = time.time() + float(sectime)
            reminder = message.content.split(' ', 2)[2]
            print(rawtime)
            print(sectime)
            await message.channel.send("fine, I'll remind you '%s' in %s , you forgetfull shit" % (reminder, rawtime))
            while int(time.time()) != int(remindtime):
                print(remindtime)
                print(time.time())
                await asyncio.sleep(1)
            await message.channel.send(reminder)

        if message.content == 's!test':
            await message.channel.send('kill me now')

        if message.content == 's!sad':
            image = images[random.randint(0,len(images)-1)]
            file= discord.File('images/'+ image, filename = image) 
            await message.channel.send('this is so sad can we get 50 likes', file=file)

        if message.content == 's!help':
            await message.channel.send(''' I'm the one that fucking needs help here

`s!test` just verifies that I'm working properly
`s!role` crowns you a bona fide sad nigga
`s!remind H:MM:SS reminder` sends _reminder_ with the specified delay
`s!sad` posts a random sad image 
`s!help` does . . . you fucking know what it does
            ''')
   

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(images)
    await client.get_channel(454457353463529482).send("bot nominal. why must you bring me into this cruel world?")


print("debug 1")
client.loop.create_task(timed_message())
print("debug 2")
client.run('NDU2MjA3MDQ3NDgyOTMzMjUx.DhGs0A.Ksf4TYVvTjPriDx1zVVtjNcpQaQ')
print("debug 3")
