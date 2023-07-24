# packages
import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os
import requests
import json

# initial setup
config = {
    "Prefix": ".",
    "Status": "Femboys",
}

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=config["Prefix"], intents=intents)

femboys = 0

# events
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=config["Status"]))

@bot.event
async def on_guild_join(guild):
    channel = guild.system_channel
    if channel:
        embed = discord.Embed(title="Hello!", description="Yahoo! My name is Astolfo! Rider Class! And, and...umm, nice to meet you!")
        embed.add_field(name="Help", value=f"If you need help, you can run the ``{config['Prefix']}help`` command!", inline=False)
        embed.add_field(name="Have fun!", value="I hope you have fun using me!", inline=False)
        embed.add_field(name="Notice", value="Please note that I may occasionally send NSFW content.")
        embed.set_thumbnail(url="https://i.pinimg.com/736x/50/77/1f/50771f45b1c015cfbb8b0853ba7b8521.jpg")
        embed.set_footer(text="Made by FireStreaker2", icon_url="https://media.discordapp.net/attachments/739313608923807844/1096169389339967618/image0.jpg")

        await channel.send(embed=embed)
    else:
        print(f"Unable to send welcome message in {guild.name}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Hm? Is it tough not having any common sense? Well, I guess so. But you know, there are things that only I can understand because I lack common sense. (you forgot to add all the arguments)")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("master, i couldnt find that command")
    else:
        await ctx.send(f"An error occurred: {error}")

# commands
@bot.command(help="Find a femboy near you!")
async def find(ctx, query):
    if isinstance(ctx.channel, discord.DMChannel) or (isinstance(ctx.channel, discord.TextChannel) and ctx.channel.is_nsfw()):
        response = requests.get(f"https://femboyfinder.firestreaker2.gq/api/{query}")
        data = response.json()
        status = data.get("Status")

        # error handling
        if response.status_code != 200 or status != 200:
            embed = discord.Embed(title="An Error Occurred", description="Hey, hey, Master! Something's up, let's go check it out!")
            embed.add_field(name="Internal Server Error", value="500: no femboys found")
            embed.set_thumbnail(url="https://i.pinimg.com/736x/50/77/1f/50771f45b1c015cfbb8b0853ba7b8521.jpg")
            embed.set_footer(text="Made by FireStreaker2", icon_url="https://media.discordapp.net/attachments/739313608923807844/1096169389339967618/image0.jpg")

            await ctx.send(embed=embed)
            return

        
        image = data.get("URL")
        dimensions = data.get("Dimensions")

        embed = discord.Embed(title="Femboy Found!")
        embed.add_field(name="Query", value=query, inline=False)
        embed.add_field(name="Dimensions", value=dimensions, inline=False)
        embed.set_image(url=image)
        embed.set_footer(text="Made by FireStreaker2", icon_url="https://media.discordapp.net/attachments/739313608923807844/1096169389339967618/image0.jpg")

        await ctx.send(embed=embed)
        global femboys
        femboys += 1

    else:
        embed = discord.Embed(title="Error", description="This channel is not marked as NSFW. In order to succesfully run this command, please mark this channel as NSFW and rerun this command.")
        embed.set_thumbnail(url="https://i.pinimg.com/736x/50/77/1f/50771f45b1c015cfbb8b0853ba7b8521.jpg")
        embed.set_footer(text="Made by FireStreaker2", icon_url="https://media.discordapp.net/attachments/739313608923807844/1096169389339967618/image0.jpg")

        await ctx.send(embed=embed)
        return

@bot.command(help="About FemboyFinderBot")
async def about(ctx):
    embed = discord.Embed(title="About", description="FemboyFinderBot is a bot developed by firestreaker2, using Discord.py. It works by querying the Danbooru API for images given the value provided by the end user, and randomly selects one.")
    embed.add_field(name="More Resources", value="For more info, you may refer to the [GitHub Page](https://github.com/FireStreaker2/FemboyFinderBot)", inline=False)
    embed.set_thumbnail(url="https://i.pinimg.com/736x/50/77/1f/50771f45b1c015cfbb8b0853ba7b8521.jpg")
    embed.set_footer(text="Made by FireStreaker2", icon_url="https://media.discordapp.net/attachments/739313608923807844/1096169389339967618/image0.jpg")

    await ctx.send(embed=embed)

@bot.command(help="Bot Statistics")
async def stats(ctx):
    embed = discord.Embed(title="Stats")
    embed.add_field(name="Guilds", value=f"I am currently in {len(bot.guilds)} servers.", inline=False)
    embed.add_field(name="Femboys", value=f"I have found {femboys} femboys so far.", inline=False)
    embed.set_thumbnail(url="https://i.pinimg.com/736x/50/77/1f/50771f45b1c015cfbb8b0853ba7b8521.jpg")
    embed.set_footer(text="Made by FireStreaker2", icon_url="https://media.discordapp.net/attachments/739313608923807844/1096169389339967618/image0.jpg")

    await ctx.send(embed=embed)

## custom help message
bot.remove_command("help")
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="Help for FemboyFinderBot")
    embed.add_field(name="Prefix", value=f"``{config['Prefix']}``", inline=False)
    embed.add_field(name=f"{config['Prefix']}find [query]", value=f"Find a femboy!\nExample: ``{config['Prefix']}find astolfo``\n\n> Note that if you are trying to search with a term that has more than one word, use a ``_`` instead of a space.\n> Example: ``{config['Prefix']}search felix_argyle``", inline=False)
    embed.add_field(name=f"{config['Prefix']}about", value=f"Sends the about message.\nExample: ``{config['Prefix']}about``", inline=False)
    embed.add_field(name=f"{config['Prefix']}stats", value=f"Sends bot statistics.\nExample: ``{config['Prefix']}stats``", inline=False)
    embed.add_field(name=f"{config['Prefix']}help", value=f"Sends this message!\nExamle: ``{config['Prefix']}help``", inline=False)
    embed.set_thumbnail(url="https://i.pinimg.com/736x/50/77/1f/50771f45b1c015cfbb8b0853ba7b8521.jpg")
    embed.set_footer(text="Made by FireStreaker2", icon_url="https://media.discordapp.net/attachments/739313608923807844/1096169389339967618/image0.jpg")

    await ctx.send(embed=embed)

bot.run(TOKEN)