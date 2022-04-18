from itertools import count
from random import shuffle
import discord
from discord.ext import commands
import pystyle, discum, sys, os, time, yaml, random
from pystyle import Write, Colors
from scraper import Scraper
from multiprocessing import Process
bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    indx = 0
    if SHUFFLE == "True":
        random.shuffle(members)
    for i in members:
        indx += 1
        member = await bot.fetch_user(i)
        try:
            if current == 0:
                # FastDM
                await member.send(MESSAGE.replace("\\n", "\n"))
                Write.Print(f"[+] Sent message to {member} (Fast Mode)\n", Colors.green, interval=0)
                break
            else:
                # SlowDM
                await member.send(MESSAGE.replace("\\n", "\n"))
                Write.Print(f"[+] Sent message to {member} (Slow Mode)\n", Colors.green, interval=0)
                time.sleep(SLEEP)
                break
        except Exception as e:
            Write.Print(f"[!] Can't send message to {member} ({e})\n", Colors.red, interval=0)
            break

if sys.platform == "linux":
    os.system("clear")
else:
    os.system("cls")
with open('./config.yml', encoding="utf-8") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
MAINTOKEN = str(config['FastDM']['scrape']['maintoken'])
GUILDID = str(config['FastDM']['scrape']['guildid'])
CHANNELID = str(config['FastDM']['scrape']['channelid'])
INVITE = str(config['FastDM']['send']['invite'])
INVITE = INVITE.replace("https://discord.gg/", "")
MESSAGE = str(config['FastDM']['send']['message'])
MODE = str(config['FastDM']['send']['mode'])
SLEEP = int(config['FastDM']['send']['sleep'])
SHUFFLE = str(config['FastDM']['send']['shuffle']) 

if MODE.lower() == "slow":
    Write.Print("FastDM 1.1U | Slow Mode\n\n", Colors.green_to_blue, interval=0.005)
    time.sleep(0.05)
    current = 1
else:
    Write.Print("FastDM 1.1U | Fast Mode\n\n", Colors.green_to_blue, interval=0.005)
    time.sleep(0.05)
    current = 0

import requests
link = INVITE
apilink = "https://discordapp.com/api/v6/invite/" + str(link)
print (link)
with open('tokens.txt','r') as handle:
    tokens = handle.readlines()
    for x in tokens:
        token = x.rstrip()
        headers={
            'Authorization': token
        }
        requests.post(apilink, headers=headers)
    print("All valid tokens have joined!")

scraper = Scraper(
    token=MAINTOKEN,
    guild_id=GUILDID,
    channel_id=CHANNELID
)
members = scraper.fetch()

if __name__ == "__main__":
    tokens = []
    with open('./tokens.txt', 'r') as f:
        tokens = f.readlines()
    print(tokens)
    while True:
        bot.run(random.choice(tokens), bot = False)