import os
import discord
from discord.ext import commands
import asyncio
import pyppeteer
from pyppeteer import launch
import gc

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='*', intents=intents)
intents.message_content = True
intents.members = True
intents.presences = True

token = ""

location_channel_id = 1076001831269961739
error_handling_channel_id = 970847761438236692
website = "https://www.goontracker.com/"

react_emote = 1077033527129944204
server_id = 770032641986002954
role_channel_id = 1076001831269961739

customsMSG = 1079267142081462323

woodsMSG = 1079267143343939595

shorelineMSG = 1079267144296038440

lighthouseMSG = 1079267145394954240

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print("Current discord.py version =", discord.__version__)

    global server
    server = bot.get_guild(server_id)
    await track_reactions(bot)
    bot.loop.create_task(update_location())


##
#####
########
###########
##############
#################
##############
###########
########
#####
##


async def track_reactions(bot):
    
    # maybe replace these
    customsROLE = discord.utils.get(bot.get_guild(server_id).roles, name='Customs')
    woodsROLE = discord.utils.get(bot.get_guild(server_id).roles, name='Woods')
    shorelineROLE = discord.utils.get(bot.get_guild(server_id).roles, name='Shoreline')
    lighthouseROLE = discord.utils.get(bot.get_guild(server_id).roles, name='Lighthouse')
    error_handling_channel = bot.get_channel(error_handling_channel_id)

    react_emote = '<:ping:1077033527129944204>'

    # define check function for on_raw_reaction_add and on_raw_reaction_remove
    async def reaction_check(payload):
        if payload.message_id in [customsMSG, woodsMSG, shorelineMSG, lighthouseMSG]:
            if str(payload.emoji) == react_emote:
                return True
        return False

    # on_raw_reaction_add event listener
    #@bot.event
    async def on_raw_reaction_add(payload):
        if await reaction_check(payload):
            guild = bot.get_guild(server_id)
            channel = guild.get_channel(role_channel_id)
            member = guild.get_member(payload.user_id)
            if member:
                if payload.message_id == customsMSG:
                    await member.add_roles(customsROLE)
                elif payload.message_id == woodsMSG:
                    await member.add_roles(woodsROLE)
                elif payload.message_id == shorelineMSG:
                    await member.add_roles(shorelineROLE)
                elif payload.message_id == lighthouseMSG:
                    await member.add_roles(lighthouseROLE)
                await error_handling_channel.send(f'{member.name} has been assigned a role for reacting to a message.')
            else:
                # the user may have left the server
                pass

    # on_raw_reaction_remove event listener
    #@bot.event
    async def on_raw_reaction_remove(payload):
        if await reaction_check(payload):
            guild = bot.get_guild(server_id)
            channel = guild.get_channel(role_channel_id)
            member = guild.get_member(payload.user_id)
            if member:
                if payload.message_id == customsMSG:
                    await member.remove_roles(customsROLE)
                elif payload.message_id == woodsMSG:
                    await member.remove_roles(woodsROLE)
                elif payload.message_id == shorelineMSG:
                    await member.remove_roles(shorelineROLE)
                elif payload.message_id == lighthouseMSG:
                    await member.remove_roles(lighthouseROLE)
                await error_handling_channel.send(f'{member.name} has had a role removed for removing a reaction from a message.')
            else:
                # the user may have left the server
                print('the user may have left the server')
                pass

    # on_raw_message_edit event listener to remove any unwanted reactions
    #@bot.event
    async def on_raw_message_edit(payload):
        if payload.message_id in [customsMSG, woodsMSG, shorelineMSG, lighthouseMSG]:
            guild = bot.get_guild(server_id)
            channel = guild.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            for reaction in message.reactions:
                if str(reaction.emoji) != react_emote:
                    async for user in reaction.users():
                        await message.remove_reaction(reaction.emoji, user)

    # add event listeners to bot
    bot.add_listener(on_raw_reaction_add)
    bot.add_listener(on_raw_reaction_remove)
    bot.add_listener(on_raw_message_edit)


##
#####
########
###########
##############
#################
##############
###########
########
#####
##

async def get_location():
    try:
        # launch a headless browser
        browser = await launch(headless=True, options={'args': ['--no-sandbox']})
        page = await browser.newPage()

        # navigate to the website
        await page.goto(website, {'waitUntil': 'networkidle0'})

        # log the HTML of the page
        html = await page.content()
        #print('Page HTML:', html)

        # wait for the page to load
        await page.waitForSelector('h5', {'timeout': 60000})

        # reload the entire page
        await page.reload()

        await asyncio.sleep(90)

        # get the location element and extract the text
        element = await page.querySelector('h5')
        location = await element.querySelectorEval('.text-danger', 'el => el.textContent')
        location = location.strip()

        if location not in ['Customs', 'Woods', 'Shoreline', 'Lighthouse']:
            raise ValueError('Location not found or not valid')

        # close the browser
        return location

    except (pyppeteer.errors.TimeoutError,
            pyppeteer.errors.NetworkError,
            pyppeteer.errors.PageError) as e:
        print(f'Error: {str(e)}. Retrying in 30 seconds...')
        await asyncio.sleep(30)
        await bot.get_channel(error_handling_channel_id).send(f"Error: {str(e)}. Retrying in 30 seconds...")
        return None
    except ValueError as e:
        print(f'Error: {str(e)}')
        await bot.get_channel(error_handling_channel_id).send(f"Error: {str(e)}")
        return None
    except Exception as e:
        print(f'Error: {str(e)}')
        await bot.get_channel(error_handling_channel_id).send(f"Error: {str(e)}")
        return None
    finally:
        await browser.close()


async def update_location():
    await bot.wait_until_ready()
    location_channel = bot.get_channel(location_channel_id)
    error_handling_channel = bot.get_channel(error_handling_channel_id)
    last_location = None  # initialize last known location as None
    last_location_message = None  # initialize last known location message as None
    while not bot.is_closed():
        location = await get_location()
        if location:
            if location != last_location:  # only update if location has changed
                role = discord.utils.get(location_channel.guild.roles, name=location)
                if role is None:
                    await error_handling_channel.send(f"Error: Role for {location} not found")
                    continue
                if last_location_message:  # delete previous message if it exists
                    await last_location_message.delete()
                last_location_message = await location_channel.send(f"Current Location: {role.mention}")
                print(f"Current Location: {location}")
                presence = discord.Game(name=f"on {location}")
                await bot.change_presence(activity=presence)
                last_location = location  # update last known location
        else:
            await error_handling_channel.send("An error occurred while trying to get the location")
        gc.collect()
        await asyncio.sleep(240)



##
#####
########
###########
##############
#################
##############
###########
########
#####
##


@bot.command()
async def updateroles(ctx):
    if str(ctx.author) != "Basiq#0227":
        return
    
    location_channel = bot.get_channel(location_channel_id)
    customsMSGg = await location_channel.fetch_message(customsMSG)
    woodsMSGg = await location_channel.fetch_message(woodsMSG)
    shorelineMSGg = await location_channel.fetch_message(shorelineMSG)
    lighthouseMSGg = await location_channel.fetch_message(lighthouseMSG)

    customsROLE = discord.utils.get(ctx.guild.roles, name='Customs')
    woodsROLE = discord.utils.get(ctx.guild.roles, name='Woods')
    shorelineROLE = discord.utils.get(ctx.guild.roles, name='Shoreline')
    lighthouseROLE = discord.utils.get(ctx.guild.roles, name='Lighthouse')

    # Fetch the users who reacted to each message
    custom_reactors = [user async for user in customsMSGg.reactions[0].users()]
    woods_reactors = [user async for user in woodsMSGg.reactions[0].users()]
    shoreline_reactors = [user async for user in shorelineMSGg.reactions[0].users()]
    lighthouse_reactors = [user async for user in lighthouseMSGg.reactions[0].users()]

    for member in ctx.guild.members:
        if member.bot:
            continue
        
        # Check Customs role
        if member in custom_reactors:
            if customsROLE not in member.roles:
                await member.add_roles(customsROLE)
        else:
            if customsROLE in member.roles:
                await member.remove_roles(customsROLE)

        # Check Woods role
        if member in woods_reactors:
            if woodsROLE not in member.roles:
                await member.add_roles(woodsROLE)
        else:
            if woodsROLE in member.roles:
                await member.remove_roles(woodsROLE)

        # Check Shoreline role
        if member in shoreline_reactors:
            if shorelineROLE not in member.roles:
                await member.add_roles(shorelineROLE)
        else:
            if shorelineROLE in member.roles:
                await member.remove_roles(shorelineROLE)

        # Check Lighthouse role
        if member in lighthouse_reactors:
            if lighthouseROLE not in member.roles:
                await member.add_roles(lighthouseROLE)
        else:
            if lighthouseROLE in member.roles:
                await member.remove_roles(lighthouseROLE)

    await ctx.send("Roles have been updated")

async def get_reactors(message_id):
    guild = bot.get_guild(server_id)
    channel = guild.get_channel(location_channel_id)
    message = await channel.fetch_message(message_id)
    users = []
    for reaction in message.reactions:
        if str(reaction.emoji) == react_emote:
            async for user in reaction.users():
                if not user.bot:
                    member = guild.get_member(user.id)
                    if member:
                        users.append(member)
                    else:
                        # User not found in server, ignore
                        pass
    return users


##
#####
########
###########
##############
#################
##############
###########
########
#####
##


@bot.command()
async def maps(ctx):
    if str(ctx.author) == "max":
        messages = []
        messages.append(await ctx.send('https://i.imgur.com/nFUOtv6.png'))
        messages.append(await ctx.send('https://i.imgur.com/1FJ62Qk.png'))
        messages.append(await ctx.send('https://i.imgur.com/UdEgYXj.png'))
        messages.append(await ctx.send('https://i.imgur.com/q6RO4Fc.png'))

        for message in messages:
            await message.add_reaction('<:ping:1077033527129944204>')
    else:
        await ctx.send("You do not have permission to use this command.")

@bot.command()
async def noti(ctx):
    if str(ctx.author) == "max":
        await ctx.send('If you\'d like to be pinged when the goons rotate to a specific map\nPress the <:ping:1077033527129944204> icon below the map you\'d like to be pinged on.\n<:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532><:blurpleline:1077033622982377532>')
    else:
        await ctx.send("You do not have permission to use this command.")

@bot.command()
async def ping(ctx):
    await ctx.reply(f'Pong ``{round(bot.latency * 1000)}ms``')



bot.run(token)
