import os
from datetime import datetime
from discord.ui import Button, View
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import discord
from discord.ext import commands
from check_stock import check_product_stock, get_product_link

load_dotenv()

DC_TOKEN = os.getenv('discord_bot_token')
DC_CHANNEL_ID = int(os.getenv('discord_channel_id'))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)

def get_channel():
    return bot.get_channel(DC_CHANNEL_ID)

async def run_discord_bot():
    await bot.start(DC_TOKEN)

def genLinkBtnView(label, link):
    button = Button(label=label, url=link)
    view = View()
    view.add_item(button)
    return view

async def send_discord_message(message, view):
    await bot.wait_until_ready()
    
    channel = get_channel()
    if channel:
        await channel.send(message, view=view)
        print(f"Send message: {message}")
    else:
        print("Can't find correct channel")

async def send_product_stock():
    try:
        now = datetime.now()
        formatted_time = now.strftime("%Y/%m/%d %H:%M:%S")
        isStock = check_product_stock();

        if isStock: 
            print(f"{formatted_time} Regularly check X-M5: ✅ Stock!")
            await send_discord_message("Regularly check X-M5: ✅ Stock!", genLinkBtnView('X-M5', get_product_link()))
        else:
            print(f"{formatted_time} Regularly check X-M5: ❌ No stock")
            # await send_discord_message("Regularly check X-M5: ❌ No stock", genLinkBtnView('X-M5', get_product_link()))

    except Exception as e:
        print("Error:", e)

async def schedule_check_stock():
    try:
        scheduler = AsyncIOScheduler()
        # scheduler.add_job(send_product_stock, 'interval', seconds=10)
        scheduler.add_job(send_product_stock, 'interval', minutes=1)
        scheduler.start()

        print("🚀 Start checking stock regularly...")
    except (KeyboardInterrupt, SystemExit):
        print("Stopping stock check...")
        scheduler.shutdown()

@bot.event
async def on_ready():
    print(f'🚀 Discord Bot {bot.user} Running at channel {get_channel().name}')
    await schedule_check_stock();

@bot.command()
async def xm5(ctx):
    now = datetime.now()
    formatted_time = now.strftime("%Y/%m/%d %H:%M:%S")
    isStock = check_product_stock()
    if isStock: 
        print(f"{formatted_time} Manually check X-M5: ✅ Stock!")
        await ctx.send("Manually check X-M5: ✅ Stock!", view=genLinkBtnView('X-M5', get_product_link()))
    else:
        print(f"{formatted_time} Manually check X-M5: ❌ No stock")
        await ctx.send("Manually check X-M5: ❌ No stock", view=genLinkBtnView('X-M5', get_product_link()))