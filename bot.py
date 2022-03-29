from discord import *
import logging
import json

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='/home/pi/ShplackBotPy/logs/shplackbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = Intents.default()
intents.members = True
intents.guilds = True


class MyClient(Client):
    async def on_ready(self):
        print('Logged on as', self.user)
            
    async def on_member_join(self, member):
        guild = member.guild
        print(guild.id)
        print(member.name)
        if guild.id == 943592028925722654: # shplack's server
            await member.edit(nick='shplack')
            
            if member.bot:
                roles = [role for role in await guild.fetch_roles() if role.name == 'Bots']
                if roles:
                    member.add_roles(roles[0])
            
            if not member.bot and not member.name not in [role.name for role in await guild.fetch_roles()]:
                member.add_roles(await guild.create_role(name=member.name, colour=Colour.random(), mentionable=True))
                

with open('token.json') as token_file:
    global token, bot
    token = json.load(token_file)['token']
    bot = MyClient(intents=intents)
    bot.run(token)