from nextcord import Webhook
import nextcord
import random
import time
from nextcord.ext import commands
import aiohttp
from nextcord.webhook.async_ import AsyncWebhookAdapter
import asyncio
theurl = open('url.txt', 'r').read
client = commands.Bot(command_prefix='-')
lines = open('randoms.txt', 'r').readlines()

async def sendToWebhook(content):
    async with aiohttp.ClientSession as session:
        webhook = nextcord.Webhook.from_url(theurl, session=session)
        await webhook.send(content)


@client.event
async def on_ready():
    while True:
        num = random.randint(1, 22)
        for linecount, x in enumerate(lines(), start=1):
            if linecount == num:
                line = x
        sendToWebhook( f'Hello <@&908912623188336700> we would revive the chat with a topic.The topic is : {line}')
        await asyncio.sleep(3600)


tokenyes = open('token.txt', 'r').read()
client.run(tokenyes)