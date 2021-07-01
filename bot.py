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


@bot.command(name="quad", help="Solutions of quadratic eqn given a, b and c")
async def quad(ctx, a: float, b: float, c: float):
    det = (b**2) - (4*a*c)
    # Not a quadratic equation
    if a == 0:
        await ctx.send("Not a quadratic equation")

    # Case of real and unequal roots
    elif det > 0:
        x1 = round((-b + (det**0.5)) / (2*a), 4)
        x2 = round((-b - (det**0.5)) / (2*a), 4)
        await ctx.send("x1 = {}".format(x1))
        await ctx.send("x2 = {}".format(x2))

    # Case of equal roots
    elif det == 0:
        x = round((-b)/(2*a), 4)
        await ctx.send("x1 = x2 = {}".format(x))

    # Case of complex roots
    elif det < 0:
        x = round((-b) / (2*a), 4)
        y = round(abs(((-det)**0.5) / (2*a)), 4)
        z1 = complex(x, y)
        z2 = complex(x, -y)
        await ctx.send("x1 = {}".format(z1))
        await ctx.send("x2 = {}".format(z2))


@bot.command(name="wolfram", help="Searches Wolfram-Alpha")
async def wolfram(ctx, *args):
    await ctx.send("{} on Wolfram-Alpha: https://www.wolframalpha.com/input/?i={}".format(' '.join(args), '+'.join(args)))


with open("TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
