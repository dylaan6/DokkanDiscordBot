import random
import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands

# ----------------------
# CONFIG
# ----------------------
TOKEN = 'YOURBOTTOKENHERE!!!' 
PREFIX = '!'  # Command prefix

# ----------------------
# LIST OF LR CARD IDs
# ----------------------
LR_IDS = [
    1007471, 1008801, 1009231, 1009381, 1009631,
    1010071, 1010161, 1010441, 1010901, 1011141, 
    1011641, 1011681, 1011721, 1012131, 1012161,
    1012361, 1012401, 1012721, 1012901, 1012931,
    1013101, 1013391, 1013771, 1014021, 1014051, 
    1014081, 1014211, 1014221, 1014471, 1014501,
    1014941, 1014971, 1015031, 1015181, 1015571,
    1016811, 1016841, 1016871, 1017321, 1017351,
    1017381, 1017631, 1017781, 1017901, 1018031,
    1018251, 1018491, 1018591, 1018621, 1018651, 
    1018881, 1019001, 1019071, 1019101, 1019401, 
    1019531, 1019701, 1019821, 1019911, 1031921, 
    1031821, 1031721, 1031591, 1031501, 1031471, 
    1031431, 1031391, 1031281, 1031221, 1030971, 
    1030791, 1030571, 1030531, 1030481, 1030431, 
    1030391, 1030341, 1030021, 1029831, 1029701, 
    1029551, 1029511, 11029471, 1029441, 1029401,
    1029361, 1029271, 1029091, 1029051, 1028961,
    1028921, 1028891, 1028721, 1028551, 1028371,
    1028321, 1028061, 1028021, 1027981, 1027601, 
    1027581, 1026391, 1026161, 1026131, 1025871,
    1025771, 1025731, 1027471, 1027461, 1027331,
    1027291, 1027221, 1027121, 1027041, 1026901,
    1026821, 1026731, 102661, 11026431, 1025651, 
    1025631, 1025591, 1025561, 1024931, 1024891, 
    1024861, 1024831, 1024731, 1024661, 1024551, 
    1024511, 1024351, 1024141, 1023891, 1023861, 
    1023621, 1023521, 1023091, 1023041, 1022941, 
    1022811, 1022781, 1022751, 1022631, 1022591, 
    1022421, 1022381, 1022341, 1022421, 1022591, 
    1022191, 1022121, 1022091, 1021971, 1021651, 
    1021621, 1021481, 1021431, 1021141, 1021011, 
    1020751, 1020461, 1020371, 1020341, 1020311, 
    1020221, 1019991, 1021881
]

# ----------------------
# FUNCTION TO FETCH RANDOM LR
# ----------------------
def get_random_lr():
    random_id = random.choice(LR_IDS)
    url = f"https://dokkaninfo.com/cards/{random_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get card name
        name_tag = soup.find('h1')
        name = name_tag.text.strip() if name_tag else f"LR Card {random_id}"

        return {
            "name": name,
            "url": url
        }

    except Exception as e:
        print(f"Error fetching LR card: {e}")
        return {
            "name": f"LR Card {random_id}",
            "url": url
        }

# ----------------------
# SET UP DISCORD BOT
# ----------------------
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def randomlr(ctx):
    lr = get_random_lr()
    embed = discord.Embed(
        title=lr['name'],
        url=lr['url'],
        description="Here's a random LR card from Dokkan Battle!"
    )
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    ultra = [
        "https://tenor.com/view/vegito-ultra-vegito-super-vegito-dragon-ball-legends-gif-26196377",
        "https://tenor.com/view/ultra-ssgss-gogeta-dbl-dragon-ball-legends-card-animation-gogeta-blue-gif-15759179547573749889",
        "https://tenor.com/view/goku-black-goku-zamasu-dbs-dragon-ball-super-gif-9307832354152930078",
        "https://tenor.com/view/broly-broly-z-ultra-dragon-ball-legends-ink-art-gif-8924254076369094817",
        "https://tenor.com/view/ultra-turles-blu-turles-dbl-turles-turles-turles-vs-goku-gif-18300471124419282253",
        "https://tenor.com/view/goku-ultra-instinct-acey-gif-14659632855809077657",
        "https://tenor.com/view/kioken-gif-4907455744812039272",
        "https://tenor.com/view/gohan-anger-ink-art-gif-4719208870913362119",
        "https://tenor.com/view/ultra-majin-vegeta-yel-majin-vegeta-umv-ultra-vegeta-yel-vegeta-gif-8096124565646510108",
        "https://tenor.com/view/db-legends-gif-26236068",
        "https://tenor.com/view/dragon-ball-legends-ultra-super-saiyan-four-super-saiyan-4-gogeta-gif-16472914923137268959",
        "https://tenor.com/view/omega-shenron-dragon-ball-legends-db-legends-legends-shenron-gif-9707217089254449472",
        "https://tenor.com/view/ultra-vegeta-pur-vegeta-vegeta-namek-vegeta-intro-gif-14266479971075100953",
        "https://tenor.com/view/ultragogeta-dragonballlegendsgogeta-dragon-ball-legends-ultra-gogeta-dragon-ball-legends-gogeta-ultra-gif-24251598",
        "https://tenor.com/view/hit-dbs-gif-8257862375585110849",
        "https://tenor.com/view/buu-kid-buu-vs-vegeta-bomb-pink-gif-21709754",
        "https://tenor.com/view/dragon-ball-legends-vegito-dbl-ssgss-gif-12224170571704374715",
        "https://tenor.com/view/ultra-janemba-blu-janemba-janemba-super-janemba-janemba-yell-gif-14813697967008488958",
        "https://tenor.com/view/ultra-golden-frieza-pur-golden-frieza-golden-frieza-frieza-golden-frieza-transformation-gif-7268259786383785333",
        "https://tenor.com/view/ultra-frieza-grn-frieza-ultra-full-power-frieza-grn-full-power-frieza-frieza-gif-4455303747926331263",
        "https://tenor.com/view/dragon-ball-legends-dragon-ball-ultra-cell-dbz-gif-18321015978904341437",
        "https://tenor.com/view/lf-ultimate-gohan-red-ultimate-gohan-lf-beast-gohan-red-beast-gohan-beast-gohan-gif-4454617038487566108",
        "https://tenor.com/view/ultra-ssj4-vegeta-red-ssj4-vegeta-ssj4-vegeta-vegeta-ssj4-gif-1496518758322709670",
        "https://tenor.com/view/ul-ss-goku-dbl-ss-goku-super-saiyan-goku-dont-you-dare-talk-about-krillin-ultra-ssj-goku-gif-2673121190051993914"
    ]


    # Convert message content to lowercase for easy matching
    content = message.content.lower()

    # Respond if the message contains triggers
    if "ultra" in message.content.lower():
        await message.channel.send(random.choice(ultra))

    # Important: Make sure commands still work
    await bot.process_commands(message)

def get_random_category():
    cat_id = random.randint(1, 97)  # IDs go from 1–97
    return {
        "name": f"Category {cat_id}",  # you can replace this with real names if you want
        "url": f"https://dokkaninfo.com/categories/{cat_id}"
    }

# ----------------------
# COMMANDS
# ----------------------
@bot.command()
async def randomcategory(ctx):
    category = get_random_category()
    embed = discord.Embed(
        title=category["name"],
        url=category["url"],
        description="Here's a random category from Dokkan Battle!"
    )
    await ctx.send(embed=embed)

def get_linkskill():
   valid_ids = list(range(1, 131)) + list(range(1000, 1005))  
   link_id = random.choice(valid_ids)
   return {
        "name": f"Link Skill {link_id}",  # Placeholder name
        "url": f"https://dokkaninfo.com/links/{link_id}"
    }

# ----------------------
# COMMANDS
# ----------------------
@bot.command()
async def randomlink(ctx):
    link = get_linkskill()
    embed = discord.Embed(
        title=link["name"],
        url=link["url"],
        description="Here's a random Link Skill from Dokkan Battle!"
    )
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    dbmovie = [
    "https://www.imdb.com/title/tt7961060/",
    "https://www.imdb.com/title/tt14614892/",
    "https://www.imdb.com/title/tt0142251/",
    "https://www.imdb.com/title/tt3819668/",
    "https://www.imdb.com/title/tt1125254/",
    "https://www.imdb.com/title/tt0142235/",
    "https://www.imdb.com/title/tt0142243/",
    "https://www.imdb.com/title/tt0142233/",
    "https://www.imdb.com/title/tt0142250/",
    "https://www.imdb.com/title/tt0142240/",
    "https://www.imdb.com/title/tt2263944/",
    "https://www.imdb.com/title/tt0142242/",
    "https://www.imdb.com/title/tt0142236/",
    "https://www.imdb.com/title/tt0142238/",
    "https://www.imdb.com/title/tt0142239/",
    "https://www.imdb.com/title/tt0142234/",
    "https://www.imdb.com/title/tt0142244/",
    "https://www.imdb.com/title/tt1317478/",
    "https://www.imdb.com/title/tt0142248/",
    "https://www.imdb.com/title/tt0142247/",
    "https://www.imdb.com/title/tt0142232/",
    "https://www.imdb.com/title/tt0142241/",
    "https://www.imdb.com/title/tt0142237/",
    "https://www.imdb.com/title/tt1098327/",
    "https://www.imdb.com/title/tt0142245/",
    "https://www.imdb.com/title/tt2980736/",
    "https://www.imdb.com/title/tt0142249/"
]



    # Convert message content to lowercase for easy matching
    content = message.content.lower()

    # Respond if the message contains triggers
    if "dbmovie" in message.content.lower():
        await message.channel.send(random.choice(dbmovie))

    # Important: Make sure commands still work
    await bot.process_commands(message)



# ----------------------
# RUN BOT
# ----------------------
bot.run(TOKEN)
