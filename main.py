from discord_webhook import DiscordWebhook, DiscordEmbed
import random
import time
theurl = open('url.txt', 'r').read
webhook = DiscordWebhook(url=theurl, content='e')
lines = open('randoms.txt', 'r').readlines()

while True:
    
    linenum = random.randint(1,22)

    for linecount, x in enumerate(lines, start=1):
        if linecount == linenum:
            line = x

    embed = DiscordEmbed(title="Dead Chat Revive", description=line, color='03b2f8')
    webhook.add_embed(embed)
    webhook.execute()
    time.sleep(3600)

