#initial build adapted from freeCodeCamp.org youtube video: https://youtu.be/SPTfmiYiuok

#Description/Goal: a discord bot that will allow users to create and manage a 'betting' pool. Users will be able to create new pools with a starting value and then other users will be able to add a certain amount of value to the pool. At the end of the event, the pool will pay out a value to the winning user, which is agreed upon by the pool manager/creator and the entrants.

import os
from replit import db
from Pool import pool
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
# GLOBALS
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
bot_token = os.environ['botToken']
client = discord.Client()
poolList = []
commandsList = ['$newPool', '$poolList', '$hello', '$commands']


#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
# FUNCTIONS
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
def nameInUse(newName):
	for x in poolList:
		name = x.getName()
		if (name == newName):
			return True
	return False


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	#load saved pools from DB


#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
# BOT EVENTS
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
@client.event
async def on_message(msg):
	if msg.author == client.user:
		return

	if msg.content.startswith('$hello'):
		await msg.channel.send('Hello')

	if msg.content.startswith('$newPool'):
		#Extract the parts of the command
		comAr = msg.content.split()
		if (len(comAr) > 3):
			await msg.channel.send(
			    'Invalid Form. Use "$newPool [name] [value]"')
			return
		name = comAr[1]
		value = comAr[2]
		#If pool name already exists, reject
		if (not nameInUse(name)):
			#create new pool
			newPool = pool(name, value)
			poolList.append(newPool)
			await msg.channel.send('Created: ' + name + ':' + value)
			#TODO: add to database for retrieval in case bot dies.
			return
		await msg.channel.send('Failed to Create: ' + name + ':' + value +
		                       ' [NAME ALREADY IN USE]')

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

	#return the list of commands
	if msg.content.startswith('$commands'):
		print(commandsList)
		await msg.channel.send(commandsList)


#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
# Main Loop
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
client.run(bot_token)
