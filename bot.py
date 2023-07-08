import discord
from discord.ext import commands

import responses

intents = discord.Intents.all()  # Enable all gateway intents
bot = commands.Bot(command_prefix='?', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is Rollin')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    username = str(message.author)
    user_message = str(message.clean_content)

    print(f"Received message: {user_message}")

    if user_message.startswith('?'):
        user_message = user_message[1:]
        print(f"Sending private message: {user_message}")
        await send_response(message, user_message, is_private=True)
    else:
        print(f"Sending public message: {user_message}")
        await send_response(message, user_message, is_private=False)

    await bot.process_commands(message)


async def send_response(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if response.strip():
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    bot.run('MTEyNzE5ODc4OTQwNTUxNTgyNg.G9OreH.DrheukuKVg9jj4Qe5VIJVo1wtJMF88_mA_D928')
