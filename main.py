import discord
import asyncio
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='*')
token = "ODA3NjYwODk2MzgxMzA0ODYy.YB7O0w.9t3vOfDcDz2PGkyPQ5qEbpS-hBI"

@bot.event
async def on_ready():
    print('the bot is ready')

    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'על {members} אנשים'
    ))
  

#mute
@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, mute_time : int, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    channel=bot.get_channel(807668030510465034)
    await channel.send(f'**Muted** {member.mention}\n**Reason: **{reason}\n**Duration:** {mute_time}m')

    embed = discord.Embed(color=discord.Color.green())
    embed.add_field(name=f"קיבלת **Muted** בשרת {ctx.guild.name}.", value=f"**על ידי: **{ctx.author.mention}\n**בגלל: **{reason}\n**לכמות זמן של:** {mute_time}m")
    await member.send(embed=embed)


    (mute_time) = (mute_time)*60
    await asyncio.sleep(mute_time)
    await member.remove_roles(role)
    channel=bot.get_channel(807668030510465034)
    await channel.send(f"**Unmuted {member.mention}**")


#vmute
@bot.command()
@commands.has_permissions(manage_messages=True)
async def vmute(ctx, member: discord.Member, mute_time : int, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Vmuted")
    await member.add_roles(role)
    channel=bot.get_channel(807668030510465034)
    await channel.send(f'**Vmuted** {member.mention}\n**Reason: **{reason}\n**Duration:** {mute_time}m')
    embed = discord.Embed(color=discord.Color.green())
    embed.add_field(name=f"קיבלת **Vmuted** בשרת {ctx.guild.name}.", value=f"**על ידי: **{ctx.author.mention}\n**בגלל: **{reason}\n**לכמות זמן של:** {mute_time}m")
    await member.send(embed=embed)
 
   
    (mute_time) = (mute_time)*60
    await asyncio.sleep(mute_time)
    await member.remove_roles(role)
    channel=bot.get_channel(807668030510465034)
    await channel.send(f"**Unvmuted {member.mention}**")


  #claer   
@bot.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int = -1):
   if amount == None:
       await ctx.channel.purge(limit=0)
   else:
       await ctx.channel.purge(limit=amount)


    
#The below code bans player.
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    channel=bot.get_channel(807668030510465034)
    await channel.send(f"**ban {member.mention}**")

#kick
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    channel=bot.get_channel(807668030510465034)
    await channel.send(f"**kick {member.mention}**")


#invites
@bot.command()
async def invites(ctx, user = None):
  if user == None:
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"הזמנת {totalInvites} אנשים{'' if totalInvites == 1 else ''}  לשרת הזה!")
  else:
    totalInvites = 0
    for i in await ctx.guild.invites():
       member = ctx.message.guild.get_member_named(user)
       if i.inviter == member:
         totalInvites += i.uses
    await ctx.send(f"{member} has invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")

from replit import db

#help
@bot.command(aliases=['עזרה', 'helpme'])
async def h(ctx, *, say, ):
    await ctx.send(f"**צריך את העזרה שלכם <@{str(ctx.author.id)}> <@&806946512637657178> **\n סיבה:`{say}`")


@h.error
async def h_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"**<@{str(ctx.author.id)}> <@&806946512637657178>  צריך את העזרה שלכם! **\nסיבה: :name_badge: **לא נרשמה סיבה** :name_badge:")     


@bot.command(aliases=['קעזרה', 'vhelpme'])
async def vh(ctx, *, say, ):
    await ctx.send(f"**צריך את העזרה שלכם <@{str(ctx.author.id)}> <@&806946512637657178> **\n סיבה:`{say}`\n המשתמש נמצא בחדר: `{str(ctx.author.voice.channel)}` ")



@vh.error
async def vh_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"**<@{str(ctx.author.id)}> <@&806946512637657178>  צריך את העזרה שלכם! **\nסיבה: :name_badge: **לא נרשמה סיבה** :name_badge:\nהמשתמש נמצא בחדר: `{str(ctx.author.voice.channel)}`")




keep_alive()
bot.run(token)
