from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.command(name="online", help="Checks if bot is online")
async def online(ctx):
    await ctx.send("Yep, I'm online!")


@bot.command(name="calc", help="Performs a calculation with +,-,*,/ or ^")
async def calc(ctx, x: float, fn: str, y: float):
    if fn == '+':
        await ctx.send(x+y)
    elif fn == '-':
        await ctx.send(x-y)
    elif fn == '*':
        await ctx.send(x*y)
    elif fn == '/':
        await ctx.send(x/y)
    elif fn == '^':
        await ctx.send(x**y)
    else:
        await ctx.send("Function is currently unaccepted")


with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
