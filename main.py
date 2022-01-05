from discord_webhook import DiscordWebhook, DiscordEmbed
import random
import time
url = open('url.txt', 'r').read

webhook = DiscordWebhook(url=url, content='<@&908912623188336700>')


while True:
    linenum = random.randint(1,22)
    lines = open('random.txt', 'r').readlines
    linecount = 0
    for x in lines:
        linecount += 1
        if linecount == linenum:
            line = x

    embed = DiscordEmbed(title="Dead Chat Revive", description=line, color='03b2f8')
    webhook.add_embed(embed)
    webhook.execute()
    time.sleep(3600)

