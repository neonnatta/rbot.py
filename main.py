# bot.py
import re
import os
import random
from replit import db
from tqdm import tqdm
from time import sleep
import discord
GUILD="Bot Testing"
TOKEN="OTg0MDA4MTk4OTA0MjE3NjIy.GWpiJU.1ljCODZJvX5CzlvRVg92XwDV8PxCLPktJ03iEw"
client = discord.Client()


m=morbius
responses = []
badwords = ["nigg", "fuck", "fuk", "fuc", 'bitch', 'ass', 'azz', 'a$$', 'damn', 'dayum', 'nij', 'shit', 'shid','$hit', '$hid', 'nlgg']


  
for i in tqdm (range(45), 
                desc="Establishing connection..", 
                ascii=False, ncols=76):
        sleep(0.03)
@client.event
async def on_connect():
    
    print("Connected to Discord!\n")
    for i in tqdm (range(113), 
                    desc="Finishing...", 
                    ascii=False, ncols=82):
            sleep(0.01)
                      
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
          
    
    print(
        m,
        f'{client.user} is connected to {guild.name} | SERVERINFO: {guild.name} : {guild.id}\n'
        
    )

safechatting=False
@client.event
async def on_message(message):
    global safechatting
    global badwords
    global responses
    if safechatting:
      for word in badwords:
        if word in message.content.lower():
          await message.channel.send("BAD WORD DETECTED!")
    if message.content.startswith('.thumb'):
        channel = message.channel
        await channel.send('React 👍 NOW!')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎👎👎')
        else:
            await channel.send('👍')
         
    msg = message.content
 


    if msg.startswith(".safechat"):
      toggle = msg.split(".safechat ",1)[1]
      print(toggle)
      if toggle.lower() == "off":
        if safechatting == True:
          safechatting = False
          await message.channel.send("Safechat disabled.")
        else:
          await message.channel.send("Safechat already disabled.")
      elif toggle.lower() == "on":
        if safechatting == False:
          safechatting = True
          await message.channel.send("Safechat enabled.")
        else:
          await message.channel.send("Safechat already enabled.")

    if msg.startswith(".repeat "):
      copy = msg.split(".repeat ",1)[1]
      sep = re.split(" : ",copy)
      amount = int(sep[1])
      word = sep([0])
      repeating=True
      while repeating:
        if amount==0:
          repeating=False
        elif amount!=0:
          await message.channel.send(word)
          amount-=1
    
    
    if msg.startswith(".cmds"):
      await message.channel.send("**My Commands:**")

    


          
client.run(TOKEN)
