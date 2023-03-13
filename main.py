import os, discord, asyncio, pytz
from datetime import datetime
from dotenv import load_dotenv
from timezone import getTime
load_dotenv()

tz = os.getenv('TIMEZONE')
tz = getTime(tz)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(schedule_morning_greeting())
    
@client.event
async def schedule_morning_greeting():
    await client.wait_until_ready()
    while not client.is_closed():
        cTZ = pytz.timezone(tz)
        now = datetime.now(tz=cTZ)
        if now.hour == 0 and now.minute == 0:
            channel = client.get_channel(int(os.getenv('CHANNEL_ID')))
            await channel.send("Good morning")
        await asyncio.sleep(60)

client.run(os.getenv("TOKEN"))
