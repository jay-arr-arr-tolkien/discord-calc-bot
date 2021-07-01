# discord-calc-bot
A basic calculator bot

## Installation
1. Clone the repository using `git clone https://github.com/jay-arr-arr-tolkien/discord-calc-bot/`
2. Ensure you have `python3` and `pip` installed. If not, follow the steps shown [here](https://stackoverflow.com/a/6587528).
3. Install the requirements using `pip install -r requirements.txt` or `python3 -m pip install -r requirements.txt`
4. Change the working directory using `cd discord-calc-bot`.
5. Follow the steps shown [here](https://www.writebots.com/discord-bot-token/) to create the bot, get its token and add it to a server.
6. Create a file `TOKEN.txt` using `touch TOKEN.txt`. Paste the token in the first line of this file.
7. That's it! Running the program using `python bot.py` should bring the bot online!

## Directly adding to server
[Link](https://discord.com/api/oauth2/authorize?client_id=855362241750106133&permissions=3072&scope=bot) to add to a server without installation. Please note that the bot is currently hosted on my personal machine, and won't be available 24x7. 

## Usage
Prefix is '!'.
Supported commands are:
1. !online: Checks whether the bot is online

![Using !online](images/online.png?raw=true "Online")

2. !calc: Peforms arithmetic on two numbers (+, -, *, / and ^ are currently supported)

![Using !calc](images/calc.png?raw=true "Calc")

3. !quad: Finds the roots of a quadratic equation with coefficients a, b and c

![Using !quad](images/quad.png?raw=true "Quad")
