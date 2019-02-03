# Rock's Bot by me

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix="r#")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="r# | Rock's Bot"))
    await bot.remove_command("help")
    print (bot.user.name)
    print (bot.user.id)

@bot.command(pass_context=True)
@commands.has_role("Moderators")
async def kick(ctx, user: discord.Member):
    await bot.say("{} has been kicked!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def ban(ctx, user: discord.Member):
    await bot.say("{} has been banned!".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
@commands.has_role("Owner")
async def rules(ctx):
    embed = discord.Embed(title="Rules", description="Server rules, the law.", color=0xc54b46)
    embed.add_field(name="Rule 1", value="No swearing.")
    embed.add_field(name="Rule 2", value="Use kind words to each other.")
    embed.add_field(name="Rule 3", value="Give your own opinions to the bot.")
    embed.add_field(name="Rule 4", value="Don't send hate if you don't like the bot.")
    embed.add_field(name="Rule 5", value="HAVE FUN!!!!")
    embed.add_field(name="**Staff Rules**", value="Rules of staff")
    embed.add_field(name="Rule 1", value="Don't abuse your power or get demoted.")
    embed.add_field(name="Rule 2", value="Do what you must.")

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def cmds(ctx):
    embed = discord.Embed(title="Commands", description="Bot commands.", color=0xc54b46)
    embed.add_field(name="kick", value="Kicks someone out of the server.")
    embed.add_field(name="ban", value="Bans somone out of the server.")
    embed.add_field(name="pat", value="Pats someone.")
    embed.add_field(name="hug", value="Hugs someone.")
    embed.add_field(name="slap", value="Slaps someone.")
    embed.add_field(name="highfive", value="High fives someone!")
    embed.add_field(name="push", value="Pushes someone off the edge.")
    embed.add_field(name="trip", value="Make someone trip.")
    embed.add_field(name="f", value="FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    embed.add_field(name="invite", value="Sends the bot invite link.")
    embed.add_field(name="damn", value="DAMN")
    embed.add_field(name="jumpoff", value="suicide")
    embed.add_field(name="suicide", value="same as jumpoff but dieeeeeeeeeee?")
    embed.add_field(name="hi", value="hi")

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def pat(ctx, user: discord.Member):
    await bot.say("Rock has patted {}!".format(user.name))
    embed = discord.Embed(title="Pat", description="Why are you looking here?", color=0xc54b46)
    embed.set_image(url='https://media1.tenor.com/images/88ff65d668f92f6d953dbffcbed2be5f/tenor.gif')

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    await bot.say("Rock has hugged {}!".format(user.name))
    embed = discord.Embed(title="Hug", description="uhhhhhhhhhhhhh", color=0xc54b46)
    embed.set_image(url='https://media1.tenor.com/images/2d4138c7c24d21b9d17f66a54ee7ea03/tenor.gif')

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def slap(ctx, user: discord.Member):
    await bot.say("Rock has slapped {}!".format(user.name))
    embed = discord.Embed(title="Slapped", description="ow", color=0xc54b46)
    embed.set_image(url='https://media.tenor.com/images/f3ee55ed3b97267c8bcc5be435bae6ac/tenor.gif')

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def highfive(ctx, user: discord.Member):
    await bot.say("Rock has high fived {}!".format(user.name))
    embed = discord.Embed(title="high five", description="wheres the battle bus?", color=0xc54b46)
    embed.set_image(url='https://media1.tenor.com/images/561c7697f4ec8ba0fd2fc8fb3ff85506/tenor.gif')

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def push(ctx, user: discord.Member):
    await bot.say("Rock has pushed {}!".format(user.name))
    embed = discord.Embed(title="push", description="did u drop in lava?", color=0xc54b46)
    embed.set_image(url='https://media1.tenor.com/images/c6656643f794a640ef16a78ed303b4fb/tenor.gif')

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def trip(ctx, user: discord.Member):
    await bot.say("Someone has made {} trip.".format(user.name))
    embed = discord.Embed(title="trip", description="watch your foot idiot", color=0xc54b46)
    embed.set_image(url='https://media1.tenor.com/images/670091eb9d2cd9747a3c390b5b98f133/tenor.gif')

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def f(ctx):
    await bot.say("ffffffffffffffffffffffffffffffffffffffffffffff")
    embed = discord.Embed(title="FFFFFFFFFFFFFFFFFFFFFFFFFF", description="ffff", color=0xc54b46)
    embed.set_image(url="https://media1.tenor.com/images/34bd2ec942b039011b2854a93d5f084a/tenor.gif")

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say("https://discordapp.com/oauth2/authorize?client_id=537451229123706881&permissions=2146958847&scope=bot")

@bot.command(pass_context=True)
async def damn(ctx):
    await bot.say("**DAMN**")

@bot.command(pass_context=True)
async def jumpoff(ctx):
    await bot.say("*jumps off*")
    embed = discord.Embed(title="i commit suicide", description="suicide", color=0xc54b46)
    embed.set_image(url="https://media1.tenor.com/images/79f427954c609c3a7f8f7be001e75d7f/tenor.gif")

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def suicide(ctx):
    await bot.say("commit suicide")
    embed = discord.Embed(title="i commit suicide too", description="suicide", color=0xc54b46)
    embed.set_image(url="https://media1.tenor.com/images/90218906927770417ab118e00c7928cd/tenor.gif")

@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("hi ( ͡° ͜ʖ ͡°)")
    embed = discord.Embed(title="hi", description="hi", color=0xc54b46)
    embed.set_image(url="https://media1.tenor.com/images/e397b58a9d2317c5d1e3c8aed71c28ac/tenor.gif")

    await bot.say(embed=embed)

bot.run("NTQxNDk2MDA5MzAyMjEyNjEz.DzgTBg.X1ExYQ-raI3_QO20ex2qrSGKdKo")
