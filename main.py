import os
import discord
# check .lock file to confirm the use of discord.py 2.0
from discord import app_commands

MY_GUILD = discord.Object(id=98252354004149756) # replace with your guild ID

# Connecting to Client
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents, application_id: int):
        super().__init__(intents=intents, application_id=application_id)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.all()
client = MyClient(intents=intents, application_id=4154365568626549756) # replace with your bot's ID

@client.event
async def on_ready():
    print(f"Logged in as {client.user}\nUser id: {client.user.id}")

# Slash command
@client.tree.command(name="help")
async def suggestion(interaction: discord.Interaction):
  embed = discord.Embed(title= "How to translate !!")
  embed.add_field(name="React with the flag", value=":flag_in:")
  await interaction.response.send_message(embed=embed, ephemeral=True)
  # ephemeral=True message will be visible to only the user

# Token
token = os.environ['TOKEN']
try:
    client.run(token)
except:
    os.system("kill 1")