#adapted from freeCodeCamp.org youtube video: https://youtu.be/SPTfmiYiuok

import os
from replit import db
from Pool.py import pool
import discord

bot_token = os.environ['botToken']

client = discord.Client()

poolList = []

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  #load saved pools from DB

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return
  if msg.content.startswith('$hello'):
    await msg.channel.send('Hello')
  if msg.content.startswith('$newPool'):
    # Extract the parts of the command
    name = 'pool'
    value = '100'
    #create new pool and add to DB
    newPool = pool(name, value)
    poolList.append(newPool)

    

client.run(bot_token)

