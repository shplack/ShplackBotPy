from discord import *
import json

intents = Intents.default()
intents.members = True
intents.guilds = True


class MyClient(Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            print(message.guild.id)
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            
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
                
        elif guild.id == 957889665380282418: # ingenjör bois
            pass
                

with open('token.json') as token_file:
    global token, bot
    token = json.load(token_file)['token']
    bot = MyClient(intents=intents)
    bot.run(token)