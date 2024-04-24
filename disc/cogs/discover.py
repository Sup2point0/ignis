'''
Implements the `/discover` family of slash commands.
'''

import os
import random
from base64 import b64decode
from io import BytesIO

import nextcord as disc
from nextcord import Embed, SlashOption
from nextcord import ui
from nextcord.ext import commands

from github import Github, Auth
from github.Repository import Repository
from github.ContentFile import ContentFile
from github.GithubException import UnknownObjectException

import suptools as sup
from .. import dyna


## NOTE Since PyGithub is synchronous (blocking), we lazy load as much as possible for these commands - first execution per lifetime may be slow as a result.


class Discover(commands.Cog):
  '''Commands relating to discovering my custom Yu-Gi-Oh creations.'''

  def __init__(self, bot):
    self.bot = bot

    self.content: dict[str, dict[str, str | dict]] = {
      "cards": None,
      "archetypes": None,
    }
    '''Content from Assort.'''


  ## utils ##
  class Keyless(Exception):
    '''GitHub API key not found.'''

  async def _load_content_(self, ctx):
    '''Synchronously fetch content from Assort through the GitHub API.
    
    This will only be called once per bot lifespan.
    '''

    # change it from `None`, so that we know we’re already loading
    self.content["archetypes"] = {}

    key = os.getenv("CYNEX")
    if key is None:
      await ctx.send("Error: Failed connecting to GitHub!")
      raise Discover.Keyless("cynex connection failed!")

    with Github(auth = Auth.Token(key)) as git:
      repo = git.get_repo("Sup2point0/Assort")
      
      content_archetypes = repo.get_contents("Yu-Gi-Oh!/archetypes/")
    
    archetypes = [
      (file, sup.io.isplitlines_base64(file.content))
      for file in content_archetypes if not "readme" in file.name.casefold()
    ]

    self.content["archetypes"] = {
      name: {
        "name": content[0].replace("# ", ""),
        "content": content,
        "path": file.path
      }
      for file, content in archetypes
    }


  ## /discover ##
  @ disc.slash_command()
  async def discover(self, ctx):
    pass


  ## /discover archetype ##
  @ discover.subcommand()
  async def archetype(self, ctx,
    archetype: str = SlashOption(
      "archetype", "name of the archetype",
      required = False, default = None,
    ),
  ):
    '''discover a custom archetype'''

    if self.content["archetypes"] is None:
      await ctx.response.defer()
      await self._load_data_(ctx)

    if archetype is None:
      archetype = random.choice(self.content["archetypes"].keys())

    archetypes = (key.casefold() for key in self.content["archetypes"])

    try:
      found = archetypes[archetype.casefold()]
    except KeyError:
      await ctx.send("No archetype with this name found" + dyna.punct.select(), ephemeral = True)
      return
    
    for line in found["content"]:
      sup.log(line = line)

      desc = b64decode(line)

    await ctx.send(embed = Embed(
      title = found["name"],
      url = "https://github.com/Sup2point0/Assort/blob/origin/" + found["path"],
      description = desc,
      colour = 0x40f190,
    ))
