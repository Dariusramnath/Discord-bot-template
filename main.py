import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 239044446535024651  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content

    msg_parts = msg.split(' ')

    if msg_parts[0] == '!kiwami':
        # number validation
        try:
            token_id = int(msg_parts[1])
        except:
            await message.channel.send('Invalid Token ID')

        if token_id >= 0 and token_id < 10000:
            base_url = f'https://frames-app-theta.vercel.app/api/p/kiwami/{str(token_id)}'
            await message.channel.send(base_url)
        else:
            await message.channel.send('Token ID outside of range')

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot