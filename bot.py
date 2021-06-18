from discord.ext import commands
import cmath

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
    # Not a quadratic equation
    if a == 0:
        await ctx.send("Not a quadratic equation")

    det = (b**2) - (4*a*c)
    
    # Case of real and unequal roots
    if det > 0:
        x_1 = (-b + (det**0.5)) / (2*a)
        x_2 = (-b - (det**0.5)) / (2*a)
        await ctx.send("x1 = ", x_1, "\n", "x2 = ", x_2)
        
    # Case of equal roots
    elif det == 0:
        await ctx.send("x1 = x2 = ", (-b)/(2*a))
        
    # Case of complex roots
    elif det < 0:
        x = (-b) / (2*a)
        y = abs(((-det)**0.5) / (2*a))
        z1 = complex(x, y)
        await ctx.send("x1 = ", z1.real, " + ", z1.imag, "i")
        await ctx.send("x2 = ", z1.real, " - ", z1.imag, "i")


with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
