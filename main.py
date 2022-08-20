# bot.py
import re
import os
import random
from replit import db
from tqdm import tqdm
from time import sleep
from colors import ansi
import discord
from morbb import morbius
GUILD="Bot Testing"
TOKEN="OTg0MDA4MTk4OTA0MjE3NjIy.GWpiJU.1ljCODZJvX5CzlvRVg92XwDV8PxCLPktJ03iEw"
client = discord.Client()


m=morbius
responses = []
badwords = ["nigg", "fuck", "fuk", "fuc", 'bitch', 'ass', 'azz', 'a$$', 'damn', 'dayum', 'nij', 'shit', 'shid','$hit', '$hid', 'nlgg']

def update_cmds(newresponse):
  if "responses" in db.keys():
    responses = db["responses"]
    responses.append(newresponse)
    db["responses"] = responses
  else:
    db["responses"] = [newresponse]

def add_badword(newword):
  if "badwords" in db.keys():
    badwords = db["badwods"]
    badwords.append(newword)
    db["badwords"] = badwords
  else:
    db["badwords"] = [badwords]
    
def delete_cmd(index):
  index -= 1
  responses = db["responses"]
  if len(responses) > index:
    del responses[index]
    db["responses"] = responses

def clear_cmd():
  responses = db["responses"]
  responses.clear()

  
for i in tqdm (range(45), 
                desc="Establishing connection..", 
                ascii=False, ncols=76):
        sleep(0.03)
@client.event
async def on_connect():
    
    print(f"\033[{ansi.bold()};{ansi.tgreen()};{ansi.bblack()} Connected to Discord!\n")
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
        f'\033[{ansi.bold()};{ansi.tgreen()};{ansi.bblack()}{client.user} is connected to {guild.name}\n'
        
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
          
    options = responses
    msg = message.content
    if msg.startswith(".clear"):
      if len(db["responses"])<1:
        await message.channel.send("No responses remaining. Use '.new [response]' to add some!")
      else:
        clear_cmd()
        await message.channel.send("Responses cleared.")

    if msg.startswith(".del"):
      responses = []
      if "responses" in db.keys():
        index = int(msg.split(".del",1)[1])
        if index!=0:
          delete_cmd(index)
          responses = db["responses"]
        else:
          await message.channel.send("Invalid item.")
      try:
        await message.channel.send(', '.join(db["responses"]))
      except:
        await message.channel.send("No responses remaining. Use '.new [response]' to add some!")
    if msg.startswith(".addswear"):
      if not safechatting:
        await message.channel.send("Unable to add. Safechat is disabled.")
      else:
        newword = msg.split(".addswear ",1)[1]
        add_badword(newword)
        await message.channel.send("New swear added to bad word list.")
    if msg.startswith(".new"):
      newresponse = msg.split(".new ",1)[1]
      update_cmds(newresponse)
      await message.channel.send("New response added.")
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
    
    if msg.startswith(".respond"):
      try:
        await message.channel.send(random.choice(db["responses"]))
      except:
        await message.channel.send("No responses remaining. Use '.new [response]' to add some!")

    if msg.startswith(".responses"):
      await message.channel.send("**My Responses:**")
      try:
        await message.channel.send(', '.join(db["responses"]))

      except:
        await message.channel.send("No responses remaining. Use '.new [response]' to add some!")
   
    if msg.startswith(".cmds"):
      await message.channel.send("**My Commands:**")
      await message.channel.send(".responses | .respond | .del [item] | .new [response] | .thumb | .clear | .safechat off/on | .addswear [swear] | .repeat [word : amount]")

    


          
client.run(TOKEN)
