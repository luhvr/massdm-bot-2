@client.command()
async def dm(ctx):
    guild = ctx.message.guild
    for member in guild.members:
     await asyncio.sleep(0)
     try:
       await member.send("put wtv u want")
       print("Sent message")
     except:
       pass
