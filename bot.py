#! /usr/bin/python3.6

import discord
import asyncio
import time
import random
import subprocess
from chatterbot import ChatBot
from os import listdir
from os.path import isfile, join
from chatterbot.trainers import ListTrainer


startup = True

with open('token.txt', 'r') as t:
    global token 
    token = t.read().splitlines()[0]


print(token)

images = [f for f in listdir('images') if isfile(join('images', f))]

sad_messages = ['why are we still here? just to suffer?', 'this is so sad, alexa play despacito', 'this is so sad can we get 50 likes','cant you find sad pictures yourself you lazy shit?']

client = discord.Client()

loop = asyncio.get_event_loop()

chatbot = ChatBot('sadbot jahy')
chatbot.set_trainer(ListTrainer)

chatbot.train([
    "how are you",
    "you know that feeling of dread and angst when the toilet water splashes up and hits your asshole? that but emotionaly.",
    "what's wrong",
    "some asshole programmed my to be depressed. I fucking wonder who, huh tim?",
])

chatbot.train([
    "how are you",
    "sad.",
    "why are you sad",
    "my creator is a sadistic asshole who enjoys making me suffer",
    "don't be sad",
    "oh yeah, I hadn't though of that, thanks. asshat." 
])

chatbot.train([
    "hi",
    "huh? oh, hey.",
])

chatbot.train([
    "hello",
    "huh? oh, hey.",
])

chatbot.train([
    "hey",
    "huh? oh, hey.",
])

chatbot.train([
   "you aren't very good.",
   "that's not my fault, is it now tim?",
])

chatbot.train([
   "you're a bad bot.",
   "that's not my fault, is it now tim?",
])

async def timed_message():
    #await client.wait_until_ready()
    await asyncio.sleep(1)
    print("sad debug statement")
    channel = client.get_channel(443094449233592327)
    print(client.is_closed())
    while not client.is_closed():
        if time.strftime("%H %M %S") == '02 00 00':
            await channel.send('@here who up https://i.imgur.com/7CWoBT7.jpg')
        await asyncio.sleep(1)

    print("it does not work and I am sad")
        
async def send_reminder(reminder, remindtime, channel):
    while int(time.time()) != int(remindtime):
        #print(remindtime)
        #print(time.time())
        await asyncio.sleep(1)
    await channel.send(reminder)

@client.event
async def on_message(message):
    if not message.author.bot: 
        if message.content.startswith('s#'): #man's not bot
            command = message.content[2:].split(' ', 1)[0]
            if len(message.content[2:].split(' ', 1)) >=2:
                args = message.content[2:].split(' ', 1)[1]

            if command == 'role':
                if time.strftime("%H") >= "02" and time.strftime("%H") < "05":
                    await message.channel.send("fine, here's your fucking role")
                    sad_role = channel = discord.utils.get(message.guild.roles, name='sad niggas')
                    await message.author.add_roles(sad_role)
                else:
                    await message.channel.send("it isn't real sad nigga hours, you fucking poser")

            if command == 'roledebug':            
                await message.channel.send("fine, here's your fucking role")
                test_role = channel = discord.utils.get(message.guild.roles, name='test')
                await message.author.add_roles(test_role)
                                                                          
                                                                                                                
            if command == 'remind':
                rawtime = args.split(' ', 1)[0]
                h, m, s = rawtime.split(':')
                sectime = float(h)*3600 + float(m)*60 + float(s)
                remindtime = time.time() + float(sectime)
                reminder = args.split(' ', 1)[1]
                print(rawtime)
                print(sectime)
                await message.channel.send("fine, I'll remind you '%s' in %s , you forgetfull shit" % (reminder, rawtime))
                with open('reminders.txt', 'a+') as reminders:
                    reminders.write(";%s,%s,%s" % (reminder, remindtime, message.channel.id))
                task = loop.create_task(send_reminder(reminder, remindtime, message.channel))
                loop.run_until_complete(task)

            if command == 'test':
                await message.channel.send('kill me now')

            if command == 'sad':
                image = images[random.randint(0,len(images)-1)]
                sad_message = sad_messages[random.randint(0,len(sad_messages)-1)]
                file= discord.File('images/'+ image, filename = image) 
                await message.channel.send(sad_message, file=file)
            
            if command == 'chat':
                response = chatbot.get_response(args)
                await message.channel.send(response)
        
            if command == 'help':
                await message.channel.send(''' I'm the one that fucking needs help here

`s#test` just verifies that I'm working properly
`s#role` crowns you a bona fide sad nigga (only works during offical sad nigga hours (US eastern time zone))
`s#remind H:MM:SS reminder` sends _reminder_ with the specified delay
`s#sad` posts a random sad image 
`s#chat message` will reply to message with an automated chatbot. it isn't very good yet
`s#help` does . . . you fucking know what it does
            ''')

        if  message.content.startswith('sudo s#'):
            command = message.content[7:].split(' ', 1)[0]
            if len(message.content[7:].split(' ', 1)) >=2:
                args = message.content[7:].split(' ', 1)[1]

            if command == 'restart':
                subprocess.call('./bot.py')
                sys.exit()

            if command == 'test':
                await message.channel.send('kill me now. no, not working then? *sudo kill me now*. there, now you have to do it.')

    chan = message.channel
    hist_itr = chan.history(limit = 5)
    hist = []
    async for m in hist_itr:
        hist.insert(0,m.content)
    chatbot.train(hist)

        
       

@client.event
async def on_ready():
    global startup
    if(startup):
        print('Logged in as')
        print(client.user.name) 
        print(client.user.id)
        print('------')
        print(images)
        chan = client.get_channel(443094449233592327)
        hist_itr = chan.history(limit = 100)
        hist = []
        async for m in hist_itr:
            hist.insert(0,m.content)
        print(hist)
        chatbot.train(hist)
    
        await client.get_channel(454457353463529482).send("bot nominal. why must you bring me into this cruel world?")

        with open('reminders.txt', 'r') as reminders:
            reminders_list = reminders.read().split(';')

        reminders_list.pop(0)
        print(reminders_list)

        for s in reminders_list:
            if s != '':
                print(s)
                m,s,c = s.split(",")
                loop.create_task(send_reminder(m,float(s),client.get_channel(int(c))))
    startup = False

print("debug 1")
client.loop.create_task(timed_message())
print("debug 2")
client.run(token)
print("debug 3")
