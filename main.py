import discord
import requests
import json
import os
from always_on import keep_alive


client = discord.Client()


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

async def on_member_join(member):
      role = discord.utils.get(member.server.roles, name = 'newbies')
      await client.add_roles(member, role)
      
    
  

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!quote'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if msg.startswith ('!version'):
    myembed = discord.Embed(
    title = "Spencer",
    description = "Hello everyone!",
    color = 0x687490
    )
    myembed.add_field(name="version code", value ="1.0.0",inline = False)
    myembed.set_author(name="Ulhas", icon_url= "https://pbs.twimg.com/profile_images/1054751689142624257/ywbp69Mg_400x400.jpg")
    await message.channel.send(embed = myembed)

  # if msg.startswith("!verify"):
  #   rol = on_member_join()
  #   await msg.run(rol)
    


 



  

keep_alive()
client.run(os.environ['KEY'])
