import requests
import datetime
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time
import logging
import secrets
import random
from discord import Webhook, RequestsWebhookAdapter
import aiohttp

now = datetime.datetime.now()

client = commands.Bot(command_prefix='!')

client.remove_command("help")


print("[BOT] Loading... | {0}".format(now.strftime("%Y-%m-%d %H:%M:%S")))
time.sleep(3)

@client.event
async def on_ready():
    print("[BOT] Expiremental Bot is ready. Waiting for bot input. | {0}".format(now.strftime("%Y-%m-%d %H:%M:%S")))
    activity = discord.Activity(name='Expiremental Bot | Online', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    time.sleep(0.5)

@client.command(pass_context=True)
async def help(ctx):
    member = ctx.message.author
    guild = ctx.message.guild
    embed2 = discord.Embed(
        colour = discord.Colour.blue()
    )
    
    embed2.set_author(name='Game Commands')
    embed2.add_field(name="!start", value="Starts a lobby. Users who join will be picked a random role, and get DM their roles.",  inline=False)
    embed2.add_field(name="!join", value="Joins users lobby.")
    await ctx.send("Sent in DMs. <@{0}>".format(ctx.message.author.id))
    await member.send(embed=embed2)
    
#needs lots of improvements
@client.command(pass_context=True)
async def game(ctx,ID:int):
    member = random.choice(ctx.guild.members)
    while True:
        member = random.choice(ctx.guild.members)
        if (member.bot == False):
            break
            
    global imposter
    imposter = member
    global gameid
    gameid = secrets.token_hex(nbytes=16)
    embed = discord.Embed(
    colour = discord.Colour.red()
    )
        
    embed2 = discord.Embed(
    colour = discord.Colour.blue()
    )

    embed3 = discord.Embed(
    colour = discord.Colour.green()
    )
    
    embed.set_author(name="You are the imposter.")
    embed.add_field(name="Your job is to kill everyone else before they finish all the tasks and not get voted out.", value="Game ID: " + gameid, inline=False)
        
    embed2.set_author(name="You are the crewmate.")
    embed2.add_field(name="Your job is to do tasks and find out who is the imposter.", value="Game ID: " + gameid, inline=False)

    embed3.set_author(name="Bot was made by Fought#3401!")
    embed3.add_field(name="The game has started!", value="Game ID: " + gameid, inline=False)

    guild = client.get_guild(ID)
    role = await guild.create_role(name=gameid)
    roleid = role.id
    global server
    server = client.get_guild(ID)
    global users
    users = []

    for member in guild.members:
        for role in member.roles:
            if (member.roles == gameid):
                users.append()

    await client.wait_until_ready()         
    member = ctx.message.author
    role = guild.get_role(roleid)
    await member.add_roles(role)

    await ctx.send("Waiting for people to join. GameID is" + gameid)
    if (len(users) == 8):
        await ctx.send(embed=embed3)
    elif (len(users) > 8):
        await ctx.send("need more members.")
    if (member.roles == gameid):
        if (len(users) == 8):
            await member.send(embed=embed)
    for member in guild.members:
        if (member.bot == False):
            if (member.roles == gameid):
                if (imposter != member):
                    if (len(users) == 8):
                        await member.send(embed=embed2)
#command above needs work too and i still need to implement if this stupid fucking users joined check or whatever, check if game ends, create private channels, do tasks command needs to be inplemented
#join command doesnt work because im still doing this stupid fucking game command
@client.command(pass_context=True)
async def join(ctx,*,gmi):
    member = ctx.message.author
    role = ctx.guild.get_role(gmi)
    await member.add_roles(role)

# this is totally fucked for now
@client.command(pass_context=True)
async def kill(ctx,*,user):
    global imposter
    if (imposter == ctx.message.author):
        for member in server.members:
            if (member.roles == gameid):
                print("it works yayayayayayay") 
            elif (imposter != ctx.message.author):
                await ctx.send("You are not the imposter.")
        
client.run("")      

