#initial build adapted from freeCodeCamp.org youtube video: https://youtu.be/SPTfmiYiuok

#Description/Goal: a discord bot that will allow users to create and manage a 'betting' pool. Users will be able to create new pools with a starting value and then other users will be able to add a certain amount of value to the pool. At the end of the event, the pool will pay out a value to the winning user, which is agreed upon by the pool manager/creator and the entrants. 

import os
from replit import db
from Pool import pool
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
    #TODO: Extract the parts of the command
    name = 'pool'
    value = '100'
    #TODO: create new pool and add to DB
    #TODO: If pool name already exists, reject
    newPool = pool(name, value)
    poolList.append(newPool)
    await msg.channel.send('Created: ' + name + ':' + value)
  
  #return the list of active pools to the user
  if msg.content.startswith('$poolList'):
    poolListString = ''
    for x in poolList:
      poolListString += ' ' + x.getName() + ':' + x.getValue() + ","
      print(poolListString)
    if poolListString:
      await msg.channel.send(poolListString)
      return
    else:
      await msg.channel.send('No active pools available.')

    

client.run(bot_token)

