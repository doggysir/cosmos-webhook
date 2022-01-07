from nextcord import Webhook
import nextcord
from random import choice
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
    lines = open('randoms.txt').read().splitlines()
    myline = choice(lines)
    await sendToWebhook(f'Hello, we would like to revive the chat with a topic. The topic is: {myline}')
    await asyncio.sleep(5)



tokenyes = open('token.txt', 'r').read()
client.run(tokenyes)