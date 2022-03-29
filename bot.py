from discord import *

class MyClient(Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            
    async def on_member_join(member):
        guild = member.guild
        if guild.id == 943592028925722654: # shplack's server
            member.nick = 'shplack'
            if not member.name not in [role.name for role in await guild.fetch_roles()]:
                member.add_roles(await guild.create_role(name=member.name, colour=Colour.random(), mentionable=True))
    
                

client = MyClient()