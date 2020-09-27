import discord
import discord.ext import commands
import discord.ext.commands import Bot
import asyncio

client.commands.Bot(command_prefix="wtv prefix u want")

client.remove_command("help")

#help command optionable(deletable)

@client.event
async def on_ready():
await client.change_presence(activity=discord.Streaming(name="wtv u want", url="enter url"))


#Stream cmd was extra yw creds to 3lone


@client.command(pass_context=True)
async def dm(ctx):
    guild = ctx.message.guild
    for member in guild.members:
     await asyncio.sleep(0)
     try:
       await member.send("wtv u want")
       print("Sent message")
     except:
       pass
client.run("token")
