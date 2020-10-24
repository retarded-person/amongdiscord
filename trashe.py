import requests
import datetime
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
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
    embed3 = discord.Embed(
        colour = discord.Colour.red()
    )
    if (ctx.message.author.id == 325849904570302469):
        embed3 = discord.Embed(
            colour = discord.Colour.blue()
        )
        
    embed2.set_author(name='Game Commands')
    embed2.add_field(name="!start", value="Starts a lobby. Users who join will be picked a random role, and get DM their roles.",  inline=False)
    embed2.add_field(name="!join", value="Joins users lobby.")
    embed3.set_author(name='Dev Commands')
    embed3.add_field(name="!leave", value="Force leave server. {id, msg}", inline=False)
    await ctx.send("Sent in DMs. <@{0}>".format(ctx.message.author.id))
    await member.send(embed=embed2)
    await member.send(embed=embed3)    

@client.command(pass_context=True)
async def leave(ctx,ID:int,msg):
    if (ctx.message.author.id == 325849904570302469):
        servers = client.guilds
        for guild in servers:
            for member in guild.members:
                if (member.bot == False):
                    embed = discord.Embed(
                   colour = discord.Colour.red()
                    )
    
                    embed.set_author(name='Bot is being force left.')
                    embed.add_field(name='Reason:', value=msg, inline=False)

                    member.send(embed=embed)
                    
                    time.sleep(1)
                    guild = client.get_guild(ID)
                    await guild.leave()

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

    await client.wait_until_ready()         
    member = ctx.message.author
    role = guild.get_role(roleid)
    await member.add_roles(role)

    await ctx.send(f"Waiting for people to join. GameID is {gameid}")
    print(f"Game has been created. GameID is {gameid}")

    while True:
        for member in guild.members:
            for role in member.roles:
                 if (member.roles == gameid):
                    users.append()
                    if (len(users) == 8):
                        break

    if (len(users) == 0):
        await ctx.send("An serious error was occured. Contact Fought#3401 with the error: ROLEERROR")
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
                
@client.command(pass_context=True)
async def join(ctx,*,gmi):
    member = ctx.message.author
    role = ctx.guild.get_role(gmi)
    if (gmi not in member.roles):
        await ctx.send("A crtical error has been found! Your brain has a mental capacity of 0!")
    roleid = role.id
    if (len(gmi) == 16):
        await member.add_roles(roleid)
        await ctx.send("Joined game.")
    elif (len(gmi) > 16):
        await ctx.send("Invalid GameID.")
                    
@client.command(pass_context=True)
async def kill(ctx,*,user):
    global imposter
    if (imposter == ctx.message.author):
        for member in server.members:
            if (member.roles == gameid):
                print("it works yayayayayayay") 
            elif (imposter != ctx.message.author):
                await ctx.send("You are not the imposter.")
        
client.run(gameid)


