from nextcord import Webhook
import nextcord
from random import randint
import time
from nextcord.ext import commands
import aiohttp
from nextcord.webhook.async_ import AsyncWebhookAdapter
import asyncio
theurl = open('url.txt', 'r').read()

client = commands.Bot(command_prefix='-jjkwdhak')
lines = open('randoms.txt', 'r').readlines

async def sendToWebhook(content):
    async with aiohttp.ClientSession() as session:
        webhook = nextcord.Webhook.from_url(theurl, session=session)
        await webhook.send(content)


@client.event
async def on_ready():
    while True:
        num = randint(1, 47)
        linecount = 0
        for x in lines():
            linecount += 1
            if linecount == num:
                line = x
        await sendToWebhook( f'Hello  we would revive the chat with a topic. The topic is : {line}')
        await asyncio.sleep(2)
        num = 1



tokenyes = open('token.txt', 'r').read()
client.run(tokenyes)