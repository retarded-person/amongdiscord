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

@client.command()
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
    embed2.add_field(name="!game", value="[!game {Server ID}] Starts a game, waits for 8 players to join and then randomly chooses one imposter from 8 people.",  inline=False)
    embed2.add_field(name="!join", value="[!join {Game ID}] Joins users lobby.")
    embed3.set_author(name='Dev Commands')
    embed3.add_field(name="!leave", value="Force leave servers that it is in. {id, msg}", inline=False)
    await ctx.send("Sent in DMs. <@{0}>".format(ctx.message.author.id))
    await member.send(embed=embed2)
    await member.send(embed=embed3)    

@client.command()
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

@client.command()
async def game(ctx):
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

    embed4 = discord.Embed(
    colour = discord.Colour.red()
    )

    embed.set_author(name="You are the imposter.")
    embed.add_field(name="Your job is to kill everyone else before they finish all the tasks and not get voted out.", value="Game ID: " + gameid, inline=False)
        
    embed2.set_author(name="You are the crewmate.")
    embed2.add_field(name="Your job is to do tasks and find out who is the imposter.", value="Game ID: " + gameid, inline=False)

    embed3.set_author(name="Bot was made by Fought#3401!")
    embed3.add_field(name="The game has started!", value="Game ID: " + gameid, inline=False)

    embed4.set_author(name="Waiting for 8 players to join.")
    embed4.add_field(name=f"Game ID: {gameid}", value = now.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    
    guild = ctx.guild
    role = await guild.create_role(name=gameid)
    roleid = role.id
    global users
    users = []

    await client.wait_until_ready()         
    member = ctx.message.author
    role = guild.get_role(roleid)
    await member.add_roles(role)

    await ctx.send(embed=embed4)
    print(f"[BOT] Game has been created.")


    for member in guild.members:
        for role in member.roles:
            if (member.roles == gameid):
                users.append()
            elif (len(users) == 8):
                break

    print(f"[BOT] Game ID: {gameid}")
    print(f"[BOT] Users currently: {len(users)}")
    
    if (len(users) == 8):
        await ctx.send(embed=embed3)
    if (member.roles == gameid):
        if (len(users) == 8):
            await member.send(embed=embed)
    for member in guild.members:
        if (member.bot == False):
            if (member.roles == gameid):
                if (imposter != member):
                    if (len(users) == 8):
                        await member.send(embed=embed2)
                
@client.command()
async def join(ctx, gameid2: discord.Role):
    if (len(gameid2.name) == 32):
        await ctx.author.add_roles(gameid2,atomic=False)
        await ctx.send("Joined game.")
    else:
        print(f"User tried to gain Role: {gameid2.name}. User is {ctx.author}")
        await ctx.send("Invalid. Stop trying it man!")
                    
@client.command()
async def kill(ctx,*,user):
    global imposter
    if (imposter == ctx.message.author):
        for member in server.members:
            if (member.roles == gameid):
                print("it works yayayayayayay") 
            elif (imposter != ctx.message.author):
                await ctx.send("You are not the imposter.")
        
client.run("awfawfawf")


