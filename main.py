import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
@client.event
async def schedule_morning_greeting():
    await client.wait_until_ready()
    while not client.is_closed():
        now = datetime.datetime.now()
        if now.hour == 0 and now.minute == 0:
            channel = client.get_channel(CHANNEL ID)
            await channel.send("Good morning")
        await asyncio.sleep(60)

client.loop.create_task(schedule_morning_greeting())

client.run(TOKEN)
