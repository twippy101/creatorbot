# %%
import discord
from discord.ext import commands
import random
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


DISCORD_TOKEN = "Njg5NTY4NjUzNDM5NTMzMDk4.X_OuBA.9wPgveQZEoB72QGeHjIA5Fsf12U"
DISCORD_GUILD = "737512359287062559"

bot = commands.Bot(command_prefix='*', self_bot = True)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="quote")
async def quote(ctx):
  starwarsquotes = ["UNLIMITED POWAAAAH", "dewit", "Oh I have a bad feeling about this", "It's over, I have the high ground", "I don't like sand"]
  response = random.choice(starwarsquotes)
  await ctx.send(response)


# %%
@bot.command(name = "create")
async def create(ctx, text, url, x:ImageFont):
    try:
        image_data = BytesIO(urlopen(url).read())
    except:
        req = Request(url, headers = {"User-Agent":"Magic Browser"})
        con = urlopen(req)
        image_data = BytesIO(con.read())
    
    img = Image.open(image_data)
    w = img.width
    h = img.height

    font = ImageFont.truetype(r"C:\Users\agupt\Downloads\Open_Sans\OpenSans-Regular.ttf", 200)
    d = ImageDraw.Draw(img)
    d.text((w/2, h-5), text, font = font, anchor = "ms", fill = (255,255,255), stroke_fill=(255,255,0))
    img.save(r"C:\Users\agupt\Downloads\meme.png")
    print("image has been created")
    await ctx.send(file=discord.File(r"C:\Users\agupt\Downloads\meme.png"))
    print("image sent")

    print(d.textsize(text,font))

@bot.command(name = "test")
async def test(ctx, text):
    print(text)

# %%
bot.run(DISCORD_TOKEN, bot = False)


# %%



